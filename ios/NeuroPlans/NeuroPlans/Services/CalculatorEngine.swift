import Foundation

/// Calculator engine that evaluates formulas for clinical calculators
enum CalculatorEngine {
    
    // MARK: - Unit Conversion Helpers
    
    /// Convert weight to kg based on selected unit
    private static func weightInKg(_ value: Double, unit: String?) -> Double {
        if unit == "lb" {
            return value / 2.205
        }
        return value  // Already kg or no unit specified
    }
    
    /// Convert height to cm based on selected unit
    private static func heightInCm(_ value: Double, unit: String?) -> Double {
        if unit == "in" {
            return value * 2.54
        }
        return value  // Already cm or no unit specified
    }
    
    /// Convert height to inches based on selected unit
    private static func heightInInches(_ value: Double, unit: String?) -> Double {
        if unit == "cm" {
            return value / 2.54
        }
        return value  // Already inches or no unit specified
    }
    
    /// Evaluate a calculator formula given its ID and input values
    /// - Parameters:
    ///   - toolId: The calculator tool ID
    ///   - vals: Dictionary of numeric input values
    ///   - selectValues: Dictionary of select/dropdown input values
    /// - Returns: The calculated result, or nil if calculation fails
    static func calculate(toolId: String, vals: [String: Double], selectValues: [String: String]) -> Double? {
        switch toolId {
        // Basic calculators
        case "corrected-phenytoin":
            return calculateCorrectedPhenytoin(vals: vals)
        case "creatinine-clearance":
            return calculateCreatinineClearance(vals: vals, selectValues: selectValues)
        case "corrected-sodium":
            return calculateCorrectedSodium(vals: vals)
        case "corrected-calcium":
            return calculateCorrectedCalcium(vals: vals)
        case "serum-osmolality":
            return calculateSerumOsmolality(vals: vals)
        case "anion-gap":
            return calculateAnionGap(vals: vals)
        case "bmi-calculator":
            return calculateBMI(vals: vals, selectValues: selectValues)
        case "ivig-dose":
            return calculateIVIgDose(vals: vals, selectValues: selectValues)
        case "temp-converter":
            return calculateTempConversion(vals: vals, selectValues: selectValues)
        case "weight-converter":
            return calculateWeightConversion(vals: vals, selectValues: selectValues)
        case "steroid-equivalence":
            return calculateSteroidEquivalence(vals: vals, selectValues: selectValues)
            
        // Neurological calculators
        case "mean-arterial-pressure":
            return calculateMAP(vals: vals)
        case "cerebral-perfusion-pressure":
            return calculateCPP(vals: vals)
        case "ich-volume-abc2":
            return calculateICHVolume(vals: vals)
        case "corrected-qtc":
            return calculateQTc(vals: vals, selectValues: selectValues)
            
        // Scoring systems
        case "wells-score-dvt":
            return calculateWellsDVT(selectValues: selectValues)
        case "wells-score-pe":
            return calculateWellsPE(selectValues: selectValues)
        case "4ts-score-hit":
            return calculate4TsHIT(selectValues: selectValues)
            
        // Fluid/electrolyte calculators
        case "free-water-deficit":
            return calculateFreeWaterDeficit(vals: vals, selectValues: selectValues)
        case "sodium-correction-rate":
            return calculateSodiumCorrectionRate(vals: vals)
        case "osmol-gap":
            return calculateOsmolGap(vals: vals)
            
        // Body measurement calculators
        case "body-surface-area":
            return calculateBSA(vals: vals, selectValues: selectValues)
        case "ideal-body-weight":
            return calculateIBW(vals: vals, selectValues: selectValues)
            
        // Specialized calculators
        case "meld-score":
            return calculateMELD(vals: vals, selectValues: selectValues)
        case "levodopa-equivalent-dose":
            return calculateLED(vals: vals, selectValues: selectValues)
        case "plasmapheresis-volume":
            return calculatePlasmapheresisVolume(vals: vals, selectValues: selectValues)
        case "predicted-fvc":
            return calculatePredictedFVC(vals: vals, selectValues: selectValues)
        case "lp-opening-pressure-correction":
            return calculateLPPressureCorrection(vals: vals, selectValues: selectValues)
            
        default:
            return nil
        }
    }
    
    // MARK: - Basic Calculators
    
    private static func calculateCorrectedPhenytoin(vals: [String: Double]) -> Double? {
        let measured = vals["measured-level"] ?? vals["measured"] ?? 0
        let albumin = vals["albumin"] ?? 4.0
        guard albumin > 0 else { return nil }
        return measured / ((0.2 * albumin) + 0.1)
    }
    
    private static func calculateCreatinineClearance(vals: [String: Double], selectValues: [String: String]) -> Double? {
        let age = vals["age"] ?? 0
        let weightRaw = vals["weight"] ?? 0
        let weight = weightInKg(weightRaw, unit: selectValues["weight-unit"])
        let cr = vals["creatinine"] ?? 1.0
        guard cr > 0 else { return nil }
        let isFemale = selectValues["sex"] == "Female"
        var result = ((140 - age) * weight) / (72 * cr)
        if isFemale { result *= 0.85 }
        return result
    }
    
    private static func calculateCorrectedSodium(vals: [String: Double]) -> Double? {
        let na = vals["sodium"] ?? 0
        let glucose = vals["glucose"] ?? 100
        return na + 0.024 * (glucose - 100)
    }
    
    private static func calculateCorrectedCalcium(vals: [String: Double]) -> Double? {
        let ca = vals["calcium"] ?? 0
        let albumin = vals["albumin"] ?? 4.0
        return ca + 0.8 * (4.0 - albumin)
    }
    
    private static func calculateSerumOsmolality(vals: [String: Double]) -> Double? {
        let na = vals["sodium"] ?? 0
        let glucose = vals["glucose"] ?? 0
        let bun = vals["bun"] ?? 0
        return (2 * na) + (glucose / 18) + (bun / 2.8)
    }
    
    private static func calculateAnionGap(vals: [String: Double]) -> Double? {
        let na = vals["sodium"] ?? 0
        let cl = vals["chloride"] ?? 0
        let hco3 = vals["bicarb"] ?? vals["bicarbonate"] ?? 0
        return na - (cl + hco3)
    }
    
    private static func calculateBMI(vals: [String: Double], selectValues: [String: String]) -> Double? {
        let weightRaw = vals["weight"] ?? 0
        let heightRaw = vals["height"] ?? 170
        let weight = weightInKg(weightRaw, unit: selectValues["weight-unit"])
        let heightCm = heightInCm(heightRaw, unit: selectValues["height-unit"])
        let heightM = heightCm / 100
        guard heightM > 0 else { return nil }
        return weight / (heightM * heightM)
    }
    
    private static func calculateIVIgDose(vals: [String: Double], selectValues: [String: String]) -> Double? {
        let weightRaw = vals["weight"] ?? 0
        let weight = weightInKg(weightRaw, unit: selectValues["weight-unit"])
        let regimen = selectValues["regimen"] ?? "Standard 5-day"
        if regimen == "2-day rapid" {
            return weight * 1.0  // 1 g/kg/day × 2 days
        }
        return weight * 0.4  // 0.4 g/kg/day × 5 days
    }
    
    private static func calculateTempConversion(vals: [String: Double], selectValues: [String: String]) -> Double? {
        let temp = vals["temperature"] ?? 0
        let unit = selectValues["unit"] ?? "°F → °C"
        if unit == "°F → °C" {
            return (temp - 32) * 5 / 9
        }
        return (temp * 9 / 5) + 32
    }
    
    private static func calculateWeightConversion(vals: [String: Double], selectValues: [String: String]) -> Double? {
        let wt = vals["weight-input"] ?? 0
        let unit = selectValues["unit"] ?? "lb → kg"
        if unit == "lb → kg" {
            return wt / 2.205
        }
        return wt * 2.205
    }
    
    private static func calculateSteroidEquivalence(vals: [String: Double], selectValues: [String: String]) -> Double? {
        let dose = vals["dose"] ?? 0
        let drug = selectValues["drug"] ?? "Prednisone"
        switch drug {
        case "Methylprednisolone": return dose * (5.0 / 4.0)
        case "Dexamethasone": return dose * (5.0 / 0.75)
        case "Hydrocortisone": return dose * (5.0 / 20.0)
        default: return dose  // Prednisone
        }
    }
    
    // MARK: - Neurological Calculators
    
    private static func calculateMAP(vals: [String: Double]) -> Double? {
        let sbp = vals["sbp"] ?? 0
        let dbp = vals["dbp"] ?? 0
        return (sbp + 2 * dbp) / 3
    }
    
    private static func calculateCPP(vals: [String: Double]) -> Double? {
        let map = vals["map"] ?? 0
        let icp = vals["icp"] ?? 0
        return map - icp
    }
    
    private static func calculateICHVolume(vals: [String: Double]) -> Double? {
        let a = vals["a"] ?? 0
        let b = vals["b"] ?? 0
        let c = vals["c"] ?? 0
        return (a * b * c) / 2
    }
    
    private static func calculateQTc(vals: [String: Double], selectValues: [String: String]) -> Double? {
        let qt = vals["qt"] ?? 0
        let inputType = selectValues["input-type"] ?? "RR interval (ms)"
        var rr = vals["rr"] ?? 0
        // Convert HR to RR interval if needed
        if inputType == "Heart rate (bpm)" && rr > 0 {
            rr = 60000 / rr
        }
        guard rr > 0 else { return nil }
        let rrSeconds = rr / 1000
        return qt / sqrt(rrSeconds)
    }
    
    // MARK: - Scoring Systems
    
    private static func calculateWellsDVT(selectValues: [String: String]) -> Double? {
        var score = 0.0
        let yesFields = ["active-cancer", "paralysis-paresis", "bedridden", "tenderness",
                        "leg-swelling", "calf-swelling", "pitting-edema", "collateral-veins", "prior-dvt"]
        for field in yesFields {
            if selectValues[field]?.hasPrefix("Yes") == true { score += 1 }
        }
        if selectValues["alternative-diagnosis"]?.hasPrefix("Yes") == true { score -= 2 }
        return score
    }
    
    private static func calculateWellsPE(selectValues: [String: String]) -> Double? {
        var score = 0.0
        if selectValues["clinical-dvt"]?.hasPrefix("Yes") == true { score += 3 }
        if selectValues["pe-likely"]?.hasPrefix("Yes") == true { score += 3 }
        if selectValues["hr-over-100"]?.hasPrefix("Yes") == true { score += 1.5 }
        if selectValues["immobilization-surgery"]?.hasPrefix("Yes") == true { score += 1.5 }
        if selectValues["prior-dvt-pe"]?.hasPrefix("Yes") == true { score += 1.5 }
        if selectValues["hemoptysis"]?.hasPrefix("Yes") == true { score += 1 }
        if selectValues["malignancy"]?.hasPrefix("Yes") == true { score += 1 }
        return score
    }
    
    private static func calculate4TsHIT(selectValues: [String: String]) -> Double? {
        var score = 0
        let categories = ["thrombocytopenia", "timing", "thrombosis", "other-causes"]
        for category in categories {
            let value = selectValues[category] ?? ""
            if value.contains("2 points") { score += 2 }
            else if value.contains("1 point") { score += 1 }
        }
        return Double(score)
    }
    
    // MARK: - Fluid/Electrolyte Calculators
    
    private static func calculateFreeWaterDeficit(vals: [String: Double], selectValues: [String: String]) -> Double? {
        let weightRaw = vals["weight"] ?? 0
        let weight = weightInKg(weightRaw, unit: selectValues["weight-unit"])
        let sodium = vals["sodium"] ?? 140
        let sex = selectValues["sex"] ?? "Male"
        let tbwFactor = sex == "Female" ? 0.5 : 0.6
        let tbw = weight * tbwFactor
        return tbw * ((sodium / 140) - 1)
    }
    
    private static func calculateSodiumCorrectionRate(vals: [String: Double]) -> Double? {
        let initial = vals["initial-sodium"] ?? 0
        let current = vals["current-sodium"] ?? 0
        let hours = vals["time-elapsed"] ?? 1
        guard hours > 0 else { return nil }
        return (current - initial) / hours
    }
    
    private static func calculateOsmolGap(vals: [String: Double]) -> Double? {
        let measuredOsm = vals["measured-osm"] ?? 0
        let na = vals["sodium"] ?? 0
        let glucose = vals["glucose"] ?? 0
        let bun = vals["bun"] ?? 0
        let ethanol = vals["ethanol"] ?? 0
        let calcOsm = (2 * na) + (glucose / 18) + (bun / 2.8) + (ethanol / 4.6)
        return measuredOsm - calcOsm
    }
    
    // MARK: - Body Measurement Calculators
    
    private static func calculateBSA(vals: [String: Double], selectValues: [String: String]) -> Double? {
        let weightRaw = vals["weight"] ?? 0
        let heightRaw = vals["height"] ?? 0
        let weight = weightInKg(weightRaw, unit: selectValues["weight-unit"])
        let height = heightInCm(heightRaw, unit: selectValues["height-unit"])
        guard weight > 0 && height > 0 else { return nil }
        return sqrt((height * weight) / 3600)
    }
    
    private static func calculateIBW(vals: [String: Double], selectValues: [String: String]) -> Double? {
        let heightRaw = vals["height"] ?? 0
        let sex = selectValues["sex"] ?? "Male"
        let heightInches = heightInInches(heightRaw, unit: selectValues["height-unit"])
        guard heightInches > 60 else { return nil }
        if sex == "Female" {
            return 45.5 + 2.3 * (heightInches - 60)
        }
        return 50 + 2.3 * (heightInches - 60)
    }
    
    // MARK: - Specialized Calculators
    
    private static func calculateMELD(vals: [String: Double], selectValues: [String: String]) -> Double? {
        var cr = max(vals["creatinine"] ?? 1.0, 1.0)
        let bili = max(vals["bilirubin"] ?? 1.0, 1.0)
        let inr = max(vals["inr"] ?? 1.0, 1.0)
        let dialysis = selectValues["dialysis"]?.hasPrefix("Yes") == true
        if dialysis || cr > 4 { cr = 4.0 }
        let meld = 10 * (0.957 * log(cr) + 0.378 * log(bili) + 1.120 * log(inr) + 0.643)
        return min(max(meld, 6), 40)
    }
    
    private static func calculateLED(vals: [String: Double], selectValues: [String: String]) -> Double? {
        var led = 0.0
        let irDose = vals["carbidopa-levodopa-ir"] ?? 0
        let crDose = vals["carbidopa-levodopa-cr"] ?? 0
        led += irDose * 1.0
        led += crDose * 0.75
        led += (vals["pramipexole"] ?? 0) * 100
        led += (vals["ropinirole"] ?? 0) * 20
        led += (vals["rotigotine"] ?? 0) * 30
        led += (vals["rasagiline"] ?? 0) * 100
        led += (vals["selegiline"] ?? 0) * 10
        led += (vals["amantadine"] ?? 0) * 1
        if selectValues["entacapone"]?.hasPrefix("Yes") == true {
            led += (irDose * 1.0 + crDose * 0.75) * 0.33
        }
        return led
    }
    
    private static func calculatePlasmapheresisVolume(vals: [String: Double], selectValues: [String: String]) -> Double? {
        let weightRaw = vals["weight"] ?? 0
        let weight = weightInKg(weightRaw, unit: selectValues["weight-unit"])
        let hct = vals["hematocrit"] ?? 40
        let exchangeStr = selectValues["exchange-volumes"] ?? "1.0"
        let exchangeRatio = Double(exchangeStr.components(separatedBy: " ").first ?? "1.0") ?? 1.0
        let plasmaVolume = weight * 70 * (1 - hct / 100)
        return plasmaVolume * exchangeRatio / 1000
    }
    
    private static func calculatePredictedFVC(vals: [String: Double], selectValues: [String: String]) -> Double? {
        let age = vals["age"] ?? 0
        let heightRaw = vals["height"] ?? 0
        let heightCm = heightInCm(heightRaw, unit: selectValues["height-unit"])
        let sex = selectValues["sex"] ?? "Male"
        if sex == "Female" {
            return (0.0443 * heightCm) - (0.026 * age) - 2.89
        }
        return (0.0576 * heightCm) - (0.026 * age) - 4.34
    }
    
    private static func calculateLPPressureCorrection(vals: [String: Double], selectValues: [String: String]) -> Double? {
        let pressure = vals["measured-pressure"] ?? 0
        let position = selectValues["position"] ?? "Lateral decubitus"
        if position == "Sitting" {
            return pressure - 15
        }
        return pressure
    }
}
