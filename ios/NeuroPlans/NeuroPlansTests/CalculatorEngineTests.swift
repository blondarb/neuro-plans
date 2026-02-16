import XCTest
@testable import NeuroPlans

/// Tests for CalculatorEngine — the static calculation engine powering
/// all medical calculators in the app.
///
/// Each test group validates a specific clinical formula against known
/// reference values and edge cases. Accuracy tolerance is 0.01 unless
/// otherwise noted.
final class CalculatorEngineTests: XCTestCase {

    // MARK: - Helpers

    /// Convenience wrapper for CalculatorEngine.calculate
    private func calc(
        _ toolId: String,
        vals: [String: Double] = [:],
        selectValues: [String: String] = [:]
    ) -> Double? {
        CalculatorEngine.calculate(toolId: toolId, vals: vals, selectValues: selectValues)
    }

    // MARK: - Corrected Phenytoin

    /// Corrected phenytoin = measured / (0.2 * albumin + 0.1)
    /// Clinical example: measured 10 mcg/mL, albumin 2.0 g/dL
    /// Expected: 10 / (0.2*2 + 0.1) = 10 / 0.5 = 20.0
    func testCorrectedPhenytoin_LowAlbumin() {
        let result = calc("corrected-phenytoin", vals: ["measured-level": 10.0, "albumin": 2.0])
        XCTAssertNotNil(result)
        XCTAssertEqual(result!, 20.0, accuracy: 0.01,
                       "Low albumin (2.0) should roughly double the corrected level")
    }

    /// Normal albumin (4.0): corrected = 10 / (0.2*4 + 0.1) = 10 / 0.9 ≈ 11.11
    func testCorrectedPhenytoin_NormalAlbumin() {
        let result = calc("corrected-phenytoin", vals: ["measured-level": 10.0, "albumin": 4.0])
        XCTAssertNotNil(result)
        XCTAssertEqual(result!, 11.11, accuracy: 0.01,
                       "Normal albumin should yield a modest correction")
    }

    /// Zero albumin should return nil (division guard)
    func testCorrectedPhenytoin_ZeroAlbumin() {
        let result = calc("corrected-phenytoin", vals: ["measured-level": 10.0, "albumin": 0.0])
        XCTAssertNil(result, "Zero albumin should return nil to avoid division by near-zero")
    }

    // MARK: - Creatinine Clearance (Cockcroft-Gault)

    /// CrCl = ((140 - age) * weight) / (72 * Cr)
    /// Male, 60 yo, 70 kg, Cr 1.0 => (80 * 70) / 72 = 77.78 mL/min
    func testCreatinineClearance_Male() {
        let result = calc("creatinine-clearance",
                          vals: ["age": 60, "weight": 70, "creatinine": 1.0],
                          selectValues: ["sex": "Male"])
        XCTAssertNotNil(result)
        XCTAssertEqual(result!, 77.78, accuracy: 0.01,
                       "60 yo male, 70 kg, Cr 1.0 should yield ~77.78 mL/min")
    }

    /// Female correction: multiply by 0.85
    /// Same patient female: 77.78 * 0.85 ≈ 66.11
    func testCreatinineClearance_Female() {
        let result = calc("creatinine-clearance",
                          vals: ["age": 60, "weight": 70, "creatinine": 1.0],
                          selectValues: ["sex": "Female"])
        XCTAssertNotNil(result)
        XCTAssertEqual(result!, 66.11, accuracy: 0.01,
                       "Female patients get a 0.85 multiplier")
    }

    /// Weight in pounds should be converted: 154 lb ≈ 69.84 kg
    func testCreatinineClearance_WeightInPounds() {
        let result = calc("creatinine-clearance",
                          vals: ["age": 60, "weight": 154, "creatinine": 1.0],
                          selectValues: ["sex": "Male", "weight-unit": "lb"])
        XCTAssertNotNil(result)
        // 154/2.205 ≈ 69.84 kg, CrCl = (80 * 69.84) / 72 ≈ 77.60
        XCTAssertEqual(result!, 77.60, accuracy: 0.5,
                       "Pound input should be auto-converted to kg")
    }

    /// Zero creatinine should return nil (division by zero protection)
    func testCreatinineClearance_ZeroCreatinine() {
        let result = calc("creatinine-clearance",
                          vals: ["age": 40, "weight": 80, "creatinine": 0.0],
                          selectValues: ["sex": "Male"])
        XCTAssertNil(result, "Zero creatinine should return nil")
    }

    // MARK: - Corrected Sodium

    /// Corrected Na = measured Na + 0.024 * (glucose - 100)
    /// Na 130, glucose 500: 130 + 0.024 * 400 = 130 + 9.6 = 139.6
    func testCorrectedSodium_Hyperglycemia() {
        let result = calc("corrected-sodium", vals: ["sodium": 130, "glucose": 500])
        XCTAssertNotNil(result)
        XCTAssertEqual(result!, 139.6, accuracy: 0.01,
                       "Glucose 500 should raise corrected sodium by ~9.6")
    }

    /// Normal glucose (100): correction = 0
    func testCorrectedSodium_NormalGlucose() {
        let result = calc("corrected-sodium", vals: ["sodium": 140, "glucose": 100])
        XCTAssertNotNil(result)
        XCTAssertEqual(result!, 140.0, accuracy: 0.01,
                       "Normal glucose should yield no correction")
    }

    // MARK: - Anion Gap

    /// AG = Na - (Cl + HCO3)
    /// Na 140, Cl 105, HCO3 24 => 140 - 129 = 11
    func testAnionGap_Normal() {
        let result = calc("anion-gap",
                          vals: ["sodium": 140, "chloride": 105, "bicarb": 24])
        XCTAssertNotNil(result)
        XCTAssertEqual(result!, 11.0, accuracy: 0.01,
                       "Normal electrolytes should yield AG ~11")
    }

    /// Elevated AG: Na 140, Cl 100, HCO3 10 => 140 - 110 = 30
    /// Seen in DKA, lactic acidosis, toxic ingestions
    func testAnionGap_Elevated() {
        let result = calc("anion-gap",
                          vals: ["sodium": 140, "chloride": 100, "bicarb": 10])
        XCTAssertNotNil(result)
        XCTAssertEqual(result!, 30.0, accuracy: 0.01,
                       "Low bicarb + normal Cl should yield high anion gap")
    }

    /// Accepts "bicarbonate" as an alternate key for HCO3
    func testAnionGap_AlternateBicarbonateKey() {
        let result = calc("anion-gap",
                          vals: ["sodium": 140, "chloride": 105, "bicarbonate": 24])
        XCTAssertNotNil(result)
        XCTAssertEqual(result!, 11.0, accuracy: 0.01,
                       "Should accept 'bicarbonate' key as an alias for 'bicarb'")
    }

    // MARK: - BMI

    /// BMI = weight(kg) / height(m)^2
    /// 70 kg, 170 cm => 70 / (1.7^2) = 70 / 2.89 ≈ 24.22
    func testBMI_NormalWeight() {
        let result = calc("bmi-calculator",
                          vals: ["weight": 70, "height": 170])
        XCTAssertNotNil(result)
        XCTAssertEqual(result!, 24.22, accuracy: 0.01,
                       "70 kg / 1.7m^2 should be ~24.22 (normal BMI)")
    }

    /// Obese: 100 kg, 170 cm => 100 / 2.89 ≈ 34.60
    func testBMI_Obese() {
        let result = calc("bmi-calculator",
                          vals: ["weight": 100, "height": 170])
        XCTAssertNotNil(result)
        XCTAssertEqual(result!, 34.60, accuracy: 0.1,
                       "100 kg at 170 cm should be obese BMI")
    }

    /// Zero height should return nil (division by zero)
    func testBMI_ZeroHeight() {
        let result = calc("bmi-calculator",
                          vals: ["weight": 70, "height": 0])
        XCTAssertNil(result, "Zero height should return nil")
    }

    /// Height in inches: 67 in = 170.18 cm
    func testBMI_HeightInInches() {
        let result = calc("bmi-calculator",
                          vals: ["weight": 70, "height": 67],
                          selectValues: ["height-unit": "in"])
        XCTAssertNotNil(result)
        // 67 in = 170.18 cm = 1.7018 m, BMI = 70/2.896 ≈ 24.17
        XCTAssertEqual(result!, 24.17, accuracy: 0.2,
                       "Height in inches should be auto-converted")
    }

    // MARK: - Mean Arterial Pressure (MAP)

    /// MAP = (SBP + 2*DBP) / 3
    /// BP 120/80: (120 + 160) / 3 = 93.33
    func testMAP_NormalBP() {
        let result = calc("mean-arterial-pressure",
                          vals: ["sbp": 120, "dbp": 80])
        XCTAssertNotNil(result)
        XCTAssertEqual(result!, 93.33, accuracy: 0.01,
                       "MAP with BP 120/80 should be ~93.33 mmHg")
    }

    /// Hypertensive urgency: BP 200/120
    /// MAP = (200 + 240) / 3 = 146.67
    func testMAP_Hypertensive() {
        let result = calc("mean-arterial-pressure",
                          vals: ["sbp": 200, "dbp": 120])
        XCTAssertNotNil(result)
        XCTAssertEqual(result!, 146.67, accuracy: 0.01,
                       "Severely elevated BP should yield high MAP")
    }

    /// Hypotensive: BP 80/50
    /// MAP = (80 + 100) / 3 = 60.0
    func testMAP_Hypotensive() {
        let result = calc("mean-arterial-pressure",
                          vals: ["sbp": 80, "dbp": 50])
        XCTAssertNotNil(result)
        XCTAssertEqual(result!, 60.0, accuracy: 0.01,
                       "MAP < 65 indicates hemodynamic instability")
    }

    // MARK: - Cerebral Perfusion Pressure (CPP)

    /// CPP = MAP - ICP
    /// MAP 90, ICP 15 => CPP 75 (normal)
    func testCPP_Normal() {
        let result = calc("cerebral-perfusion-pressure",
                          vals: ["map": 90, "icp": 15])
        XCTAssertNotNil(result)
        XCTAssertEqual(result!, 75.0, accuracy: 0.01,
                       "CPP > 60 is the clinical target")
    }

    /// Elevated ICP: MAP 80, ICP 30 => CPP 50 (dangerously low)
    func testCPP_ElevatedICP() {
        let result = calc("cerebral-perfusion-pressure",
                          vals: ["map": 80, "icp": 30])
        XCTAssertNotNil(result)
        XCTAssertEqual(result!, 50.0, accuracy: 0.01,
                       "CPP < 60 requires urgent intervention")
    }

    // MARK: - QTc (Bazett's Formula)

    /// QTc = QT / sqrt(RR in seconds)
    /// QT 400 ms, RR 800 ms => QTc = 400 / sqrt(0.8) ≈ 447.2
    func testQTc_WithRRInterval() {
        let result = calc("corrected-qtc",
                          vals: ["qt": 400, "rr": 800],
                          selectValues: ["input-type": "RR interval (ms)"])
        XCTAssertNotNil(result)
        XCTAssertEqual(result!, 447.2, accuracy: 0.1,
                       "QTc with RR 800ms should be ~447 ms")
    }

    /// QT 400 ms, HR 75 bpm => RR = 60000/75 = 800 ms => same result
    func testQTc_WithHeartRate() {
        let result = calc("corrected-qtc",
                          vals: ["qt": 400, "rr": 75],
                          selectValues: ["input-type": "Heart rate (bpm)"])
        XCTAssertNotNil(result)
        XCTAssertEqual(result!, 447.2, accuracy: 0.1,
                       "HR-based input should convert to RR and yield same QTc")
    }

    /// Zero RR should return nil
    func testQTc_ZeroRR() {
        let result = calc("corrected-qtc",
                          vals: ["qt": 400, "rr": 0],
                          selectValues: ["input-type": "RR interval (ms)"])
        XCTAssertNil(result, "Zero RR interval should return nil")
    }

    // MARK: - Serum Osmolality

    /// Serum Osm = 2*Na + Glucose/18 + BUN/2.8
    /// Na 140, glucose 100, BUN 20 => 280 + 5.56 + 7.14 = 292.7
    func testSerumOsmolality_Normal() {
        let result = calc("serum-osmolality",
                          vals: ["sodium": 140, "glucose": 100, "bun": 20])
        XCTAssertNotNil(result)
        XCTAssertEqual(result!, 292.70, accuracy: 0.1,
                       "Normal serum osmolality should be ~285-295 mOsm/kg")
    }

    /// Hypernatremia: Na 160 => 320 + 5.56 + 7.14 = 332.7
    func testSerumOsmolality_Hypernatremia() {
        let result = calc("serum-osmolality",
                          vals: ["sodium": 160, "glucose": 100, "bun": 20])
        XCTAssertNotNil(result)
        XCTAssertEqual(result!, 332.70, accuracy: 0.1,
                       "Hypernatremia should markedly elevate osmolality")
    }

    // MARK: - Corrected Calcium

    /// Corrected Ca = measured Ca + 0.8 * (4.0 - albumin)
    /// Ca 8.0, albumin 2.0 => 8.0 + 0.8 * 2.0 = 9.6
    func testCorrectedCalcium_LowAlbumin() {
        let result = calc("corrected-calcium",
                          vals: ["calcium": 8.0, "albumin": 2.0])
        XCTAssertNotNil(result)
        XCTAssertEqual(result!, 9.6, accuracy: 0.01,
                       "Low albumin should increase corrected calcium")
    }

    /// Normal albumin (4.0): no correction
    func testCorrectedCalcium_NormalAlbumin() {
        let result = calc("corrected-calcium",
                          vals: ["calcium": 9.5, "albumin": 4.0])
        XCTAssertNotNil(result)
        XCTAssertEqual(result!, 9.5, accuracy: 0.01,
                       "Normal albumin should yield no correction")
    }

    /// High albumin (5.0): correction subtracts
    func testCorrectedCalcium_HighAlbumin() {
        let result = calc("corrected-calcium",
                          vals: ["calcium": 10.5, "albumin": 5.0])
        XCTAssertNotNil(result)
        XCTAssertEqual(result!, 9.7, accuracy: 0.01,
                       "High albumin should lower corrected calcium")
    }

    // MARK: - ICH Volume (ABC/2)

    /// Volume = (A * B * C) / 2
    /// A=5, B=4, C=3 => 30 mL
    func testICHVolume_Typical() {
        let result = calc("ich-volume-abc2",
                          vals: ["a": 5, "b": 4, "c": 3])
        XCTAssertNotNil(result)
        XCTAssertEqual(result!, 30.0, accuracy: 0.01,
                       "ABC/2 volume estimation for 5x4x3 cm hemorrhage")
    }

    /// Zero dimension => 0 volume
    func testICHVolume_ZeroDimension() {
        let result = calc("ich-volume-abc2",
                          vals: ["a": 5, "b": 0, "c": 3])
        XCTAssertNotNil(result)
        XCTAssertEqual(result!, 0.0, accuracy: 0.01,
                       "Zero dimension should yield zero volume")
    }

    // MARK: - Temperature Conversion

    /// 98.6 F => 37.0 C
    func testTempConversion_FtoC() {
        let result = calc("temp-converter",
                          vals: ["temperature": 98.6],
                          selectValues: ["unit": "°F → °C"])
        XCTAssertNotNil(result)
        XCTAssertEqual(result!, 37.0, accuracy: 0.01,
                       "98.6 F should convert to 37.0 C")
    }

    /// 37.0 C => 98.6 F
    func testTempConversion_CtoF() {
        let result = calc("temp-converter",
                          vals: ["temperature": 37.0],
                          selectValues: ["unit": "°C → °F"])
        XCTAssertNotNil(result)
        XCTAssertEqual(result!, 98.6, accuracy: 0.01,
                       "37.0 C should convert to 98.6 F")
    }

    // MARK: - Steroid Equivalence

    /// Prednisone dose stays the same (reference steroid)
    func testSteroidEquivalence_Prednisone() {
        let result = calc("steroid-equivalence",
                          vals: ["dose": 20],
                          selectValues: ["drug": "Prednisone"])
        XCTAssertNotNil(result)
        XCTAssertEqual(result!, 20.0, accuracy: 0.01)
    }

    /// Dexamethasone 4 mg = Prednisone 4 * (5/0.75) ≈ 26.67 mg
    func testSteroidEquivalence_Dexamethasone() {
        let result = calc("steroid-equivalence",
                          vals: ["dose": 4],
                          selectValues: ["drug": "Dexamethasone"])
        XCTAssertNotNil(result)
        XCTAssertEqual(result!, 26.67, accuracy: 0.01,
                       "Dexamethasone is ~6.67x more potent than prednisone")
    }

    /// Methylprednisolone 1000 mg = Prednisone 1000 * (5/4) = 1250 mg
    func testSteroidEquivalence_Methylprednisolone() {
        let result = calc("steroid-equivalence",
                          vals: ["dose": 1000],
                          selectValues: ["drug": "Methylprednisolone"])
        XCTAssertNotNil(result)
        XCTAssertEqual(result!, 1250.0, accuracy: 0.01,
                       "IV methylpred 1g pulse = 1250 mg prednisone equivalent")
    }

    /// Hydrocortisone 100 mg = Prednisone 100 * (5/20) = 25 mg
    func testSteroidEquivalence_Hydrocortisone() {
        let result = calc("steroid-equivalence",
                          vals: ["dose": 100],
                          selectValues: ["drug": "Hydrocortisone"])
        XCTAssertNotNil(result)
        XCTAssertEqual(result!, 25.0, accuracy: 0.01,
                       "Hydrocortisone is 1/4 the potency of prednisone")
    }

    // MARK: - Sodium Correction Rate

    /// Rate = (current - initial) / hours
    /// Initial 118, current 124, over 12 hours => 0.5 mEq/L/hr
    func testSodiumCorrectionRate_Normal() {
        let result = calc("sodium-correction-rate",
                          vals: ["initial-sodium": 118, "current-sodium": 124, "time-elapsed": 12])
        XCTAssertNotNil(result)
        XCTAssertEqual(result!, 0.5, accuracy: 0.01,
                       "6 mEq rise over 12 hours = 0.5 mEq/L/hr (safe rate)")
    }

    /// Zero hours should return nil
    func testSodiumCorrectionRate_ZeroHours() {
        let result = calc("sodium-correction-rate",
                          vals: ["initial-sodium": 118, "current-sodium": 124, "time-elapsed": 0])
        XCTAssertNil(result, "Zero elapsed time should return nil")
    }

    // MARK: - Free Water Deficit

    /// FWD = TBW * ((Na/140) - 1), TBW = weight * 0.6 (male) or 0.5 (female)
    /// Male, 70 kg, Na 155 => TBW = 42, FWD = 42 * (155/140 - 1) = 42 * 0.1071 ≈ 4.5 L
    func testFreeWaterDeficit_Male() {
        let result = calc("free-water-deficit",
                          vals: ["weight": 70, "sodium": 155],
                          selectValues: ["sex": "Male"])
        XCTAssertNotNil(result)
        XCTAssertEqual(result!, 4.5, accuracy: 0.1,
                       "Male 70 kg with Na 155 should need ~4.5 L free water")
    }

    /// Female uses TBW factor 0.5 instead of 0.6
    func testFreeWaterDeficit_Female() {
        let result = calc("free-water-deficit",
                          vals: ["weight": 70, "sodium": 155],
                          selectValues: ["sex": "Female"])
        XCTAssertNotNil(result)
        // TBW = 35, FWD = 35 * 0.1071 ≈ 3.75
        XCTAssertEqual(result!, 3.75, accuracy: 0.1,
                       "Female uses lower TBW factor (0.5)")
    }

    // MARK: - Body Surface Area (Mosteller)

    /// BSA = sqrt((height_cm * weight_kg) / 3600)
    /// 170 cm, 70 kg => sqrt(11900/3600) = sqrt(3.306) ≈ 1.818 m^2
    func testBSA_Normal() {
        let result = calc("body-surface-area",
                          vals: ["weight": 70, "height": 170])
        XCTAssertNotNil(result)
        XCTAssertEqual(result!, 1.818, accuracy: 0.01,
                       "Average adult BSA should be ~1.7-2.0 m^2")
    }

    /// Zero weight should return nil
    func testBSA_ZeroWeight() {
        let result = calc("body-surface-area",
                          vals: ["weight": 0, "height": 170])
        XCTAssertNil(result, "Zero weight should return nil")
    }

    // MARK: - Ideal Body Weight (Devine)

    /// Male IBW = 50 + 2.3 * (height_inches - 60)
    /// 70 inches => 50 + 2.3 * 10 = 73 kg
    func testIBW_Male() {
        let result = calc("ideal-body-weight",
                          vals: ["height": 70],
                          selectValues: ["sex": "Male"])
        XCTAssertNotNil(result)
        XCTAssertEqual(result!, 73.0, accuracy: 0.01,
                       "Male 70 inches should have IBW of 73 kg")
    }

    /// Female IBW = 45.5 + 2.3 * (height_inches - 60)
    /// 65 inches => 45.5 + 2.3 * 5 = 57.0 kg
    func testIBW_Female() {
        let result = calc("ideal-body-weight",
                          vals: ["height": 65],
                          selectValues: ["sex": "Female"])
        XCTAssertNotNil(result)
        XCTAssertEqual(result!, 57.0, accuracy: 0.01,
                       "Female 65 inches should have IBW of 57 kg")
    }

    /// Height <= 60 inches should return nil (formula not valid)
    func testIBW_ShortHeight() {
        let result = calc("ideal-body-weight",
                          vals: ["height": 58],
                          selectValues: ["sex": "Male"])
        XCTAssertNil(result, "Height <= 60 inches should return nil")
    }

    /// Height in cm should be auto-converted: 170 cm = 66.93 in
    func testIBW_HeightInCm() {
        let result = calc("ideal-body-weight",
                          vals: ["height": 170],
                          selectValues: ["sex": "Male", "height-unit": "cm"])
        XCTAssertNotNil(result)
        // 170/2.54 ≈ 66.93 in, IBW = 50 + 2.3 * 6.93 ≈ 65.94
        XCTAssertEqual(result!, 65.94, accuracy: 0.5,
                       "Height in cm should be auto-converted to inches")
    }

    // MARK: - Unknown Tool ID

    /// Unrecognized tool IDs should return nil
    func testUnknownToolId() {
        let result = calc("nonexistent-calculator", vals: ["x": 1])
        XCTAssertNil(result, "Unknown tool ID should return nil")
    }

    // MARK: - IVIg Dose

    /// Standard 5-day regimen: 0.4 g/kg/day
    /// 70 kg => 28 g/day
    func testIVIgDose_Standard() {
        let result = calc("ivig-dose",
                          vals: ["weight": 70],
                          selectValues: ["regimen": "Standard 5-day"])
        XCTAssertNotNil(result)
        XCTAssertEqual(result!, 28.0, accuracy: 0.01,
                       "Standard IVIg = 0.4 g/kg/day")
    }

    /// 2-day rapid regimen: 1.0 g/kg/day
    /// 70 kg => 70 g/day
    func testIVIgDose_Rapid() {
        let result = calc("ivig-dose",
                          vals: ["weight": 70],
                          selectValues: ["regimen": "2-day rapid"])
        XCTAssertNotNil(result)
        XCTAssertEqual(result!, 70.0, accuracy: 0.01,
                       "Rapid IVIg = 1.0 g/kg/day")
    }

    // MARK: - Osmol Gap

    /// OsmGap = measured - calculated
    /// Calculated = 2*Na + glucose/18 + BUN/2.8 + ethanol/4.6
    func testOsmolGap_Normal() {
        // Na 140, glucose 100, BUN 20, ethanol 0
        // Calculated = 280 + 5.56 + 7.14 + 0 = 292.7
        // Measured 295 => gap = 2.3
        let result = calc("osmol-gap",
                          vals: ["measured-osm": 295, "sodium": 140, "glucose": 100,
                                 "bun": 20, "ethanol": 0])
        XCTAssertNotNil(result)
        XCTAssertEqual(result!, 2.3, accuracy: 0.1,
                       "Normal osmol gap should be < 10")
    }

    /// Elevated osmol gap (suggests toxic alcohol ingestion)
    func testOsmolGap_Elevated() {
        // Same calculated ≈ 292.7, measured 330 => gap ≈ 37.3
        let result = calc("osmol-gap",
                          vals: ["measured-osm": 330, "sodium": 140, "glucose": 100,
                                 "bun": 20, "ethanol": 0])
        XCTAssertNotNil(result)
        XCTAssertEqual(result!, 37.3, accuracy: 0.1,
                       "High osmol gap suggests toxic alcohol ingestion")
    }

    // MARK: - LP Opening Pressure Correction

    /// Lateral decubitus: no correction applied
    func testLPPressure_LateralDecubitus() {
        let result = calc("lp-opening-pressure-correction",
                          vals: ["measured-pressure": 20],
                          selectValues: ["position": "Lateral decubitus"])
        XCTAssertNotNil(result)
        XCTAssertEqual(result!, 20.0, accuracy: 0.01,
                       "Lateral decubitus is reference position, no correction")
    }

    /// Sitting position: subtract 15 cmH2O
    func testLPPressure_Sitting() {
        let result = calc("lp-opening-pressure-correction",
                          vals: ["measured-pressure": 30],
                          selectValues: ["position": "Sitting"])
        XCTAssertNotNil(result)
        XCTAssertEqual(result!, 15.0, accuracy: 0.01,
                       "Sitting position subtracts 15 cmH2O from measured pressure")
    }
}
