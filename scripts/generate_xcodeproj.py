#!/usr/bin/env python3
"""
Generate NeuroPlans.xcodeproj/project.pbxproj for the iOS app.

Usage:
    python3 scripts/generate_xcodeproj.py

This creates a ready-to-use Xcode project that you can open directly:
    open ios/NeuroPlans/NeuroPlans.xcodeproj
"""

import hashlib
import os
import textwrap

# ---------------------------------------------------------------------------
# Deterministic ID generator
# ---------------------------------------------------------------------------

def uid(seed: str) -> str:
    """Generate a deterministic 24-char uppercase hex ID from a seed."""
    return hashlib.sha256(f"neuroplans-xcode-{seed}".encode()).hexdigest()[:24].upper()


# ---------------------------------------------------------------------------
# Project structure definitions
# ---------------------------------------------------------------------------

# IDs for structural elements
PROJECT_ID          = uid("project")
MAIN_GROUP          = uid("main-group")
SOURCE_GROUP        = uid("source-group")          # NeuroPlans/
MODELS_GROUP        = uid("models-group")
SERVICES_GROUP      = uid("services-group")
THEME_GROUP         = uid("theme-group")
VIEWS_GROUP         = uid("views-group")
COMPONENTS_GROUP    = uid("components-group")
HOME_GROUP          = uid("home-group")
BROWSE_GROUP        = uid("browse-group")
DETAIL_GROUP        = uid("detail-group")
BUILDER_GROUP       = uid("builder-group")
FAVORITES_GROUP     = uid("favorites-group")
SETTINGS_VIEW_GROUP = uid("settings-view-group")
REFERENCE_GROUP     = uid("reference-group")
RESOURCES_GROUP     = uid("resources-group")
PRODUCTS_GROUP      = uid("products-group")
FRAMEWORKS_GROUP    = uid("frameworks-group")

# Target & phases
TARGET_ID           = uid("target")
SOURCES_PHASE       = uid("sources-phase")
RESOURCES_PHASE     = uid("resources-phase")
FRAMEWORKS_PHASE    = uid("frameworks-phase")

# Build configurations
DEBUG_PROJ          = uid("debug-project")
RELEASE_PROJ        = uid("release-project")
DEBUG_TARGET        = uid("debug-target")
RELEASE_TARGET      = uid("release-target")
CONFIG_LIST_PROJ    = uid("config-list-project")
CONFIG_LIST_TARGET  = uid("config-list-target")

# Product
PRODUCT_REF         = uid("product-ref")


# ---------------------------------------------------------------------------
# File definitions: (display_name, path_in_group, file_type, group_key)
# ---------------------------------------------------------------------------

SWIFT_FILES = [
    ("NeuroPlansApp.swift",        "NeuroPlansApp.swift",        "sourcecode.swift", "source"),
    ("Plan.swift",                 "Plan.swift",                 "sourcecode.swift", "models"),
    ("Category.swift",             "Category.swift",             "sourcecode.swift", "models"),
    ("Reference.swift",            "Reference.swift",            "sourcecode.swift", "models"),
    ("Theme.swift",                "Theme.swift",                "sourcecode.swift", "theme"),
    ("PlanStore.swift",            "PlanStore.swift",            "sourcecode.swift", "services"),
    ("PlanBuilder.swift",          "PlanBuilder.swift",          "sourcecode.swift", "services"),
    ("ReferenceStore.swift",       "ReferenceStore.swift",       "sourcecode.swift", "services"),
    ("PriorityBadge.swift",        "PriorityBadge.swift",        "sourcecode.swift", "components"),
    ("SettingPicker.swift",        "SettingPicker.swift",        "sourcecode.swift", "components"),
    ("GlassCard.swift",            "GlassCard.swift",            "sourcecode.swift", "components"),
    ("MetadataChip.swift",         "MetadataChip.swift",         "sourcecode.swift", "components"),
    ("MainTabView.swift",          "MainTabView.swift",          "sourcecode.swift", "views"),
    ("HomeView.swift",             "HomeView.swift",             "sourcecode.swift", "home"),
    ("CategoryCard.swift",         "CategoryCard.swift",         "sourcecode.swift", "home"),
    ("PlanListView.swift",         "PlanListView.swift",         "sourcecode.swift", "browse"),
    ("PlanRow.swift",              "PlanRow.swift",              "sourcecode.swift", "browse"),
    ("PlanDetailView.swift",       "PlanDetailView.swift",       "sourcecode.swift", "detail"),
    ("SectionGroup.swift",         "SectionGroup.swift",         "sourcecode.swift", "detail"),
    ("ItemRows.swift",             "ItemRows.swift",             "sourcecode.swift", "detail"),
    ("TreatmentItemRow.swift",     "TreatmentItemRow.swift",     "sourcecode.swift", "detail"),
    ("BuilderView.swift",          "BuilderView.swift",          "sourcecode.swift", "builder"),
    ("FavoritesView.swift",        "FavoritesView.swift",        "sourcecode.swift", "favorites"),
    ("SettingsView.swift",         "SettingsView.swift",         "sourcecode.swift", "settings_view"),
    ("ReferenceHomeView.swift",    "ReferenceHomeView.swift",    "sourcecode.swift", "reference"),
    ("ScaleListView.swift",        "ScaleListView.swift",        "sourcecode.swift", "reference"),
    ("ScaleDetailView.swift",      "ScaleDetailView.swift",      "sourcecode.swift", "reference"),
    ("ExamListView.swift",         "ExamListView.swift",         "sourcecode.swift", "reference"),
    ("ExamDetailView.swift",       "ExamDetailView.swift",       "sourcecode.swift", "reference"),
    ("ToolListView.swift",         "ToolListView.swift",         "sourcecode.swift", "reference"),
    ("ToolDetailView.swift",       "ToolDetailView.swift",       "sourcecode.swift", "reference"),
]

RESOURCE_FILES = [
    ("plans.json",       "plans.json",       "text.json",            "resources"),
    ("scales.json",      "scales.json",      "text.json",            "resources"),
    ("exams.json",       "exams.json",       "text.json",            "resources"),
    ("tools.json",       "tools.json",       "text.json",            "resources"),
    ("Assets.xcassets",  "Assets.xcassets",   "folder.assetcatalog",  "source"),
]

# Generate IDs for each file
file_ref_ids = {}
build_file_ids = {}
for name, _, _, _ in SWIFT_FILES + RESOURCE_FILES:
    file_ref_ids[name] = uid(f"fileref-{name}")
    build_file_ids[name] = uid(f"buildfile-{name}")


# ---------------------------------------------------------------------------
# Group → children mapping
# ---------------------------------------------------------------------------

GROUP_MAP = {
    "source":        SOURCE_GROUP,
    "models":        MODELS_GROUP,
    "services":      SERVICES_GROUP,
    "theme":         THEME_GROUP,
    "views":         VIEWS_GROUP,
    "components":    COMPONENTS_GROUP,
    "home":          HOME_GROUP,
    "browse":        BROWSE_GROUP,
    "detail":        DETAIL_GROUP,
    "builder":       BUILDER_GROUP,
    "favorites":     FAVORITES_GROUP,
    "settings_view": SETTINGS_VIEW_GROUP,
    "reference":     REFERENCE_GROUP,
    "resources":     RESOURCES_GROUP,
}


def build_group_children():
    """Build map of group_key -> list of child file ref IDs."""
    children = {k: [] for k in GROUP_MAP}
    for name, _, _, group_key in SWIFT_FILES + RESOURCE_FILES:
        children[group_key].append(file_ref_ids[name])
    return children


# ---------------------------------------------------------------------------
# pbxproj generation
# ---------------------------------------------------------------------------

def generate_pbxproj() -> str:
    group_children = build_group_children()

    lines = []
    def w(text=""):
        lines.append(text)

    w("// !$*UTF8*$!")
    w("{")
    w("\tarchiveVersion = 1;")
    w("\tclasses = {")
    w("\t};")
    w("\tobjectVersion = 56;")
    w("\tobjects = {")
    w()

    # --- PBXBuildFile ---
    w("/* Begin PBXBuildFile section */")
    for name, _, ftype, _ in SWIFT_FILES:
        w(f"\t\t{build_file_ids[name]} /* {name} in Sources */ = "
          f"{{isa = PBXBuildFile; fileRef = {file_ref_ids[name]} /* {name} */; }};")
    for name, _, ftype, _ in RESOURCE_FILES:
        w(f"\t\t{build_file_ids[name]} /* {name} in Resources */ = "
          f"{{isa = PBXBuildFile; fileRef = {file_ref_ids[name]} /* {name} */; }};")
    w("/* End PBXBuildFile section */")
    w()

    # --- PBXFileReference ---
    w("/* Begin PBXFileReference section */")
    for name, path, ftype, _ in SWIFT_FILES + RESOURCE_FILES:
        w(f'\t\t{file_ref_ids[name]} /* {name} */ = '
          f'{{isa = PBXFileReference; lastKnownFileType = {ftype}; '
          f'path = {name}; sourceTree = "<group>"; }};')
    # Product reference
    w(f'\t\t{PRODUCT_REF} /* Neuro Plans.app */ = '
      f'{{isa = PBXFileReference; explicitFileType = wrapper.application; '
      f'includeInIndex = 0; path = "Neuro Plans.app"; sourceTree = BUILT_PRODUCTS_DIR; }};')
    w("/* End PBXFileReference section */")
    w()

    # --- PBXFrameworksBuildPhase ---
    w("/* Begin PBXFrameworksBuildPhase section */")
    w(f"\t\t{FRAMEWORKS_PHASE} /* Frameworks */ = {{")
    w("\t\t\tisa = PBXFrameworksBuildPhase;")
    w("\t\t\tbuildActionMask = 2147483647;")
    w("\t\t\tfiles = (")
    w("\t\t\t);")
    w("\t\t\trunOnlyForDeploymentPostprocessing = 0;")
    w("\t\t};")
    w("/* End PBXFrameworksBuildPhase section */")
    w()

    # --- PBXGroup ---
    w("/* Begin PBXGroup section */")

    # Main group (project root)
    w(f"\t\t{MAIN_GROUP} = {{")
    w("\t\t\tisa = PBXGroup;")
    w("\t\t\tchildren = (")
    w(f"\t\t\t\t{SOURCE_GROUP} /* NeuroPlans */,")
    w(f"\t\t\t\t{PRODUCTS_GROUP} /* Products */,")
    w(f"\t\t\t\t{FRAMEWORKS_GROUP} /* Frameworks */,")
    w("\t\t\t);")
    w('\t\t\tsourceTree = "<group>";')
    w("\t\t};")

    # Products group
    w(f"\t\t{PRODUCTS_GROUP} /* Products */ = {{")
    w("\t\t\tisa = PBXGroup;")
    w("\t\t\tchildren = (")
    w(f"\t\t\t\t{PRODUCT_REF} /* Neuro Plans.app */,")
    w("\t\t\t);")
    w('\t\t\tname = Products;')
    w('\t\t\tsourceTree = "<group>";')
    w("\t\t};")

    # Frameworks group (empty)
    w(f"\t\t{FRAMEWORKS_GROUP} /* Frameworks */ = {{")
    w("\t\t\tisa = PBXGroup;")
    w("\t\t\tchildren = (")
    w("\t\t\t);")
    w('\t\t\tname = Frameworks;')
    w('\t\t\tsourceTree = "<group>";')
    w("\t\t};")

    # NeuroPlans source group
    source_direct = [fid for fid in group_children.get("source", [])]
    w(f"\t\t{SOURCE_GROUP} /* NeuroPlans */ = {{")
    w("\t\t\tisa = PBXGroup;")
    w("\t\t\tchildren = (")
    # App entry point first
    for fid in source_direct:
        for name, _, _, gk in SWIFT_FILES + RESOURCE_FILES:
            if file_ref_ids[name] == fid:
                w(f"\t\t\t\t{fid} /* {name} */,")
                break
    # Then subgroups
    w(f"\t\t\t\t{MODELS_GROUP} /* Models */,")
    w(f"\t\t\t\t{SERVICES_GROUP} /* Services */,")
    w(f"\t\t\t\t{THEME_GROUP} /* Theme */,")
    w(f"\t\t\t\t{VIEWS_GROUP} /* Views */,")
    w(f"\t\t\t\t{RESOURCES_GROUP} /* Resources */,")
    w("\t\t\t);")
    w('\t\t\tpath = NeuroPlans;')
    w('\t\t\tsourceTree = "<group>";')
    w("\t\t};")

    # Helper to write a simple group
    def write_group(gid, name, path, child_ids, subgroup_ids=None):
        w(f"\t\t{gid} /* {name} */ = {{")
        w("\t\t\tisa = PBXGroup;")
        w("\t\t\tchildren = (")
        for fid in child_ids:
            # Find the display name
            for fname, _, _, _ in SWIFT_FILES + RESOURCE_FILES:
                if file_ref_ids[fname] == fid:
                    w(f"\t\t\t\t{fid} /* {fname} */,")
                    break
        if subgroup_ids:
            for sg_id, sg_name in subgroup_ids:
                w(f"\t\t\t\t{sg_id} /* {sg_name} */,")
        w("\t\t\t);")
        w(f'\t\t\tpath = {path};')
        w(f'\t\t\tsourceTree = "<group>";')
        w("\t\t};")

    write_group(MODELS_GROUP, "Models", "Models", group_children["models"])
    write_group(SERVICES_GROUP, "Services", "Services", group_children["services"])
    write_group(THEME_GROUP, "Theme", "Theme", group_children["theme"])

    # Views group has MainTabView.swift + subgroups
    w(f"\t\t{VIEWS_GROUP} /* Views */ = {{")
    w("\t\t\tisa = PBXGroup;")
    w("\t\t\tchildren = (")
    for fid in group_children["views"]:
        for fname, _, _, _ in SWIFT_FILES:
            if file_ref_ids[fname] == fid:
                w(f"\t\t\t\t{fid} /* {fname} */,")
                break
    w(f"\t\t\t\t{COMPONENTS_GROUP} /* Components */,")
    w(f"\t\t\t\t{HOME_GROUP} /* Home */,")
    w(f"\t\t\t\t{BROWSE_GROUP} /* Browse */,")
    w(f"\t\t\t\t{DETAIL_GROUP} /* Detail */,")
    w(f"\t\t\t\t{BUILDER_GROUP} /* Builder */,")
    w(f"\t\t\t\t{FAVORITES_GROUP} /* Favorites */,")
    w(f"\t\t\t\t{SETTINGS_VIEW_GROUP} /* Settings */,")
    w(f"\t\t\t\t{REFERENCE_GROUP} /* Reference */,")
    w("\t\t\t);")
    w('\t\t\tpath = Views;')
    w('\t\t\tsourceTree = "<group>";')
    w("\t\t};")

    write_group(COMPONENTS_GROUP, "Components", "Components", group_children["components"])
    write_group(HOME_GROUP, "Home", "Home", group_children["home"])
    write_group(BROWSE_GROUP, "Browse", "Browse", group_children["browse"])
    write_group(DETAIL_GROUP, "Detail", "Detail", group_children["detail"])
    write_group(BUILDER_GROUP, "Builder", "Builder", group_children["builder"])
    write_group(FAVORITES_GROUP, "Favorites", "Favorites", group_children["favorites"])
    write_group(SETTINGS_VIEW_GROUP, "Settings", "Settings", group_children["settings_view"])
    write_group(REFERENCE_GROUP, "Reference", "Reference", group_children["reference"])
    write_group(RESOURCES_GROUP, "Resources", "Resources", group_children["resources"])

    w("/* End PBXGroup section */")
    w()

    # --- PBXNativeTarget ---
    w("/* Begin PBXNativeTarget section */")
    w(f"\t\t{TARGET_ID} /* NeuroPlans */ = {{")
    w("\t\t\tisa = PBXNativeTarget;")
    w(f"\t\t\tbuildConfigurationList = {CONFIG_LIST_TARGET} /* Build configuration list for PBXNativeTarget \"NeuroPlans\" */;")
    w("\t\t\tbuildPhases = (")
    w(f"\t\t\t\t{SOURCES_PHASE} /* Sources */,")
    w(f"\t\t\t\t{FRAMEWORKS_PHASE} /* Frameworks */,")
    w(f"\t\t\t\t{RESOURCES_PHASE} /* Resources */,")
    w("\t\t\t);")
    w("\t\t\tbuildRules = (")
    w("\t\t\t);")
    w("\t\t\tdependencies = (")
    w("\t\t\t);")
    w('\t\t\tname = NeuroPlans;')
    w(f"\t\t\tproductName = NeuroPlans;")
    w(f"\t\t\tproductReference = {PRODUCT_REF} /* Neuro Plans.app */;")
    w('\t\t\tproductType = "com.apple.product-type.application";')
    w("\t\t};")
    w("/* End PBXNativeTarget section */")
    w()

    # --- PBXProject ---
    w("/* Begin PBXProject section */")
    w(f"\t\t{PROJECT_ID} /* Project object */ = {{")
    w("\t\t\tisa = PBXProject;")
    w(f"\t\t\tbuildConfigurationList = {CONFIG_LIST_PROJ} /* Build configuration list for PBXProject \"NeuroPlans\" */;")
    w("\t\t\tcompatibilityVersion = \"Xcode 14.0\";")
    w("\t\t\tdevelopmentRegion = en;")
    w("\t\t\thasScannedForEncodings = 0;")
    w("\t\t\tknownRegions = (")
    w("\t\t\t\ten,")
    w("\t\t\t\tBase,")
    w("\t\t\t);")
    w(f"\t\t\tmainGroup = {MAIN_GROUP};")
    w(f"\t\t\tproductRefGroup = {PRODUCTS_GROUP} /* Products */;")
    w('\t\t\tprojectDirPath = "";')
    w('\t\t\tprojectRoot = "";')
    w("\t\t\ttargets = (")
    w(f"\t\t\t\t{TARGET_ID} /* NeuroPlans */,")
    w("\t\t\t);")
    w("\t\t};")
    w("/* End PBXProject section */")
    w()

    # --- PBXResourcesBuildPhase ---
    w("/* Begin PBXResourcesBuildPhase section */")
    w(f"\t\t{RESOURCES_PHASE} /* Resources */ = {{")
    w("\t\t\tisa = PBXResourcesBuildPhase;")
    w("\t\t\tbuildActionMask = 2147483647;")
    w("\t\t\tfiles = (")
    for name, _, _, _ in RESOURCE_FILES:
        w(f"\t\t\t\t{build_file_ids[name]} /* {name} in Resources */,")
    w("\t\t\t);")
    w("\t\t\trunOnlyForDeploymentPostprocessing = 0;")
    w("\t\t};")
    w("/* End PBXResourcesBuildPhase section */")
    w()

    # --- PBXSourcesBuildPhase ---
    w("/* Begin PBXSourcesBuildPhase section */")
    w(f"\t\t{SOURCES_PHASE} /* Sources */ = {{")
    w("\t\t\tisa = PBXSourcesBuildPhase;")
    w("\t\t\tbuildActionMask = 2147483647;")
    w("\t\t\tfiles = (")
    for name, _, _, _ in SWIFT_FILES:
        w(f"\t\t\t\t{build_file_ids[name]} /* {name} in Sources */,")
    w("\t\t\t);")
    w("\t\t\trunOnlyForDeploymentPostprocessing = 0;")
    w("\t\t};")
    w("/* End PBXSourcesBuildPhase section */")
    w()

    # --- XCBuildConfiguration ---
    w("/* Begin XCBuildConfiguration section */")

    # Project-level Debug
    w(f"\t\t{DEBUG_PROJ} /* Debug */ = {{")
    w("\t\t\tisa = XCBuildConfiguration;")
    w("\t\t\tbuildSettings = {")
    w("\t\t\t\tALWAYS_SEARCH_USER_PATHS = NO;")
    w("\t\t\t\tASSTETS_DIR = \"\";")
    w('\t\t\t\tCLANG_ANALYZER_NONNULL = YES;')
    w('\t\t\t\tCLANG_ANALYZER_NUMBER_OBJECT_CONVERSION = YES_AGGRESSIVE;')
    w('\t\t\t\tCLANG_CXX_LANGUAGE_STANDARD = "gnu++20";')
    w('\t\t\t\tCLANG_ENABLE_MODULES = YES;')
    w('\t\t\t\tCLANG_ENABLE_OBJC_ARC = YES;')
    w('\t\t\t\tCLANG_ENABLE_OBJC_WEAK = YES;')
    w('\t\t\t\tCLANG_WARN_BLOCK_CAPTURE_AUTORELEASING = YES;')
    w('\t\t\t\tCLANG_WARN_BOOL_CONVERSION = YES;')
    w('\t\t\t\tCLANG_WARN_COMMA = YES;')
    w('\t\t\t\tCLANG_WARN_CONSTANT_CONVERSION = YES;')
    w('\t\t\t\tCLANG_WARN_DEPRECATED_OBJC_IMPLEMENTATIONS = YES;')
    w('\t\t\t\tCLANG_WARN_DIRECT_OBJC_ISA_USAGE = YES_ERROR;')
    w('\t\t\t\tCLANG_WARN_DOCUMENTATION_COMMENTS = YES;')
    w('\t\t\t\tCLANG_WARN_EMPTY_BODY = YES;')
    w('\t\t\t\tCLANG_WARN_ENUM_CONVERSION = YES;')
    w('\t\t\t\tCLANG_WARN_INFINITE_RECURSION = YES;')
    w('\t\t\t\tCLANG_WARN_INT_CONVERSION = YES;')
    w('\t\t\t\tCLANG_WARN_NON_LITERAL_NULL_CONVERSION = YES;')
    w('\t\t\t\tCLANG_WARN_OBJC_IMPLICIT_RETAIN_SELF = YES;')
    w('\t\t\t\tCLANG_WARN_OBJC_LITERAL_CONVERSION = YES;')
    w('\t\t\t\tCLANG_WARN_OBJC_ROOT_CLASS = YES_ERROR;')
    w('\t\t\t\tCLANG_WARN_QUOTED_INCLUDE_IN_FRAMEWORK_HEADER = YES;')
    w('\t\t\t\tCLANG_WARN_RANGE_LOOP_ANALYSIS = YES;')
    w('\t\t\t\tCLANG_WARN_STRICT_PROTOTYPES = YES;')
    w('\t\t\t\tCLANG_WARN_SUSPICIOUS_MOVE = YES;')
    w('\t\t\t\tCLANG_WARN_UNGUARDED_AVAILABILITY = YES_AGGRESSIVE;')
    w('\t\t\t\tCLANG_WARN_UNREACHABLE_CODE = YES;')
    w('\t\t\t\tCLANG_WARN__DUPLICATE_METHOD_MATCH = YES;')
    w('\t\t\t\tCOPY_PHASE_STRIP = NO;')
    w('\t\t\t\tDEBUG_INFORMATION_FORMAT = dwarf;')
    w('\t\t\t\tENABLE_STRICT_OBJC_MSGSEND = YES;')
    w('\t\t\t\tENABLE_TESTABILITY = YES;')
    w('\t\t\t\tENABLE_USER_SCRIPT_SANDBOXING = YES;')
    w('\t\t\t\tGCC_C_LANGUAGE_STANDARD = gnu17;')
    w('\t\t\t\tGCC_DYNAMIC_NO_PIC = NO;')
    w('\t\t\t\tGCC_NO_COMMON_BLOCKS = YES;')
    w('\t\t\t\tGCC_OPTIMIZATION_LEVEL = 0;')
    w('\t\t\t\tGCC_PREPROCESSOR_DEFINITIONS = (')
    w('\t\t\t\t\t"DEBUG=1",')
    w('\t\t\t\t\t"$(inherited)",')
    w('\t\t\t\t);')
    w('\t\t\t\tGCC_WARN_64_TO_32_BIT_CONVERSION = YES;')
    w('\t\t\t\tGCC_WARN_ABOUT_RETURN_TYPE = YES_ERROR;')
    w('\t\t\t\tGCC_WARN_UNDECLARED_SELECTOR = YES;')
    w('\t\t\t\tGCC_WARN_UNINITIALIZED_AUTOS = YES_AGGRESSIVE;')
    w('\t\t\t\tGCC_WARN_UNUSED_FUNCTION = YES;')
    w('\t\t\t\tGCC_WARN_UNUSED_VARIABLE = YES;')
    w('\t\t\t\tIPHONEOS_DEPLOYMENT_TARGET = 17.0;')
    w('\t\t\t\tLOCALIZATION_PREFERS_STRING_CATALOGS = YES;')
    w('\t\t\t\tMTL_ENABLE_DEBUG_INFO = INCLUDE_SOURCE;')
    w('\t\t\t\tMTL_FAST_MATH = YES;')
    w('\t\t\t\tONLY_ACTIVE_ARCH = YES;')
    w('\t\t\t\tSDKROOT = iphoneos;')
    w('\t\t\t\tSWIFT_ACTIVE_COMPILATION_CONDITIONS = "$(inherited) DEBUG";')
    w('\t\t\t\tSWIFT_OPTIMIZATION_LEVEL = "-Onone";')
    w('\t\t\t\tSWIFT_VERSION = 5.9;')
    w("\t\t\t};")
    w(f'\t\t\tname = Debug;')
    w("\t\t};")

    # Project-level Release
    w(f"\t\t{RELEASE_PROJ} /* Release */ = {{")
    w("\t\t\tisa = XCBuildConfiguration;")
    w("\t\t\tbuildSettings = {")
    w("\t\t\t\tALWAYS_SEARCH_USER_PATHS = NO;")
    w("\t\t\t\tASSTETS_DIR = \"\";")
    w('\t\t\t\tCLANG_ANALYZER_NONNULL = YES;')
    w('\t\t\t\tCLANG_ANALYZER_NUMBER_OBJECT_CONVERSION = YES_AGGRESSIVE;')
    w('\t\t\t\tCLANG_CXX_LANGUAGE_STANDARD = "gnu++20";')
    w('\t\t\t\tCLANG_ENABLE_MODULES = YES;')
    w('\t\t\t\tCLANG_ENABLE_OBJC_ARC = YES;')
    w('\t\t\t\tCLANG_ENABLE_OBJC_WEAK = YES;')
    w('\t\t\t\tCLANG_WARN_BLOCK_CAPTURE_AUTORELEASING = YES;')
    w('\t\t\t\tCLANG_WARN_BOOL_CONVERSION = YES;')
    w('\t\t\t\tCLANG_WARN_COMMA = YES;')
    w('\t\t\t\tCLANG_WARN_CONSTANT_CONVERSION = YES;')
    w('\t\t\t\tCLANG_WARN_DEPRECATED_OBJC_IMPLEMENTATIONS = YES;')
    w('\t\t\t\tCLANG_WARN_DIRECT_OBJC_ISA_USAGE = YES_ERROR;')
    w('\t\t\t\tCLANG_WARN_DOCUMENTATION_COMMENTS = YES;')
    w('\t\t\t\tCLANG_WARN_EMPTY_BODY = YES;')
    w('\t\t\t\tCLANG_WARN_ENUM_CONVERSION = YES;')
    w('\t\t\t\tCLANG_WARN_INFINITE_RECURSION = YES;')
    w('\t\t\t\tCLANG_WARN_INT_CONVERSION = YES;')
    w('\t\t\t\tCLANG_WARN_NON_LITERAL_NULL_CONVERSION = YES;')
    w('\t\t\t\tCLANG_WARN_OBJC_IMPLICIT_RETAIN_SELF = YES;')
    w('\t\t\t\tCLANG_WARN_OBJC_LITERAL_CONVERSION = YES;')
    w('\t\t\t\tCLANG_WARN_OBJC_ROOT_CLASS = YES_ERROR;')
    w('\t\t\t\tCLANG_WARN_QUOTED_INCLUDE_IN_FRAMEWORK_HEADER = YES;')
    w('\t\t\t\tCLANG_WARN_RANGE_LOOP_ANALYSIS = YES;')
    w('\t\t\t\tCLANG_WARN_STRICT_PROTOTYPES = YES;')
    w('\t\t\t\tCLANG_WARN_SUSPICIOUS_MOVE = YES;')
    w('\t\t\t\tCLANG_WARN_UNGUARDED_AVAILABILITY = YES_AGGRESSIVE;')
    w('\t\t\t\tCLANG_WARN_UNREACHABLE_CODE = YES;')
    w('\t\t\t\tCLANG_WARN__DUPLICATE_METHOD_MATCH = YES;')
    w('\t\t\t\tCOPY_PHASE_STRIP = NO;')
    w('\t\t\t\tDEBUG_INFORMATION_FORMAT = "dwarf-with-dsym";')
    w('\t\t\t\tENABLE_NS_ASSERTIONS = NO;')
    w('\t\t\t\tENABLE_STRICT_OBJC_MSGSEND = YES;')
    w('\t\t\t\tENABLE_USER_SCRIPT_SANDBOXING = YES;')
    w('\t\t\t\tGCC_C_LANGUAGE_STANDARD = gnu17;')
    w('\t\t\t\tGCC_NO_COMMON_BLOCKS = YES;')
    w('\t\t\t\tGCC_WARN_64_TO_32_BIT_CONVERSION = YES;')
    w('\t\t\t\tGCC_WARN_ABOUT_RETURN_TYPE = YES_ERROR;')
    w('\t\t\t\tGCC_WARN_UNDECLARED_SELECTOR = YES;')
    w('\t\t\t\tGCC_WARN_UNINITIALIZED_AUTOS = YES_AGGRESSIVE;')
    w('\t\t\t\tGCC_WARN_UNUSED_FUNCTION = YES;')
    w('\t\t\t\tGCC_WARN_UNUSED_VARIABLE = YES;')
    w('\t\t\t\tIPHONEOS_DEPLOYMENT_TARGET = 17.0;')
    w('\t\t\t\tLOCALIZATION_PREFERS_STRING_CATALOGS = YES;')
    w('\t\t\t\tMTL_ENABLE_DEBUG_INFO = NO;')
    w('\t\t\t\tMTL_FAST_MATH = YES;')
    w('\t\t\t\tSDKROOT = iphoneos;')
    w('\t\t\t\tSWIFT_COMPILATION_MODE = wholemodule;')
    w('\t\t\t\tSWIFT_VERSION = 5.9;')
    w('\t\t\t\tVALIDATE_PRODUCT = YES;')
    w("\t\t\t};")
    w(f'\t\t\tname = Release;')
    w("\t\t};")

    # Target-level Debug
    w(f"\t\t{DEBUG_TARGET} /* Debug */ = {{")
    w("\t\t\tisa = XCBuildConfiguration;")
    w("\t\t\tbuildSettings = {")
    w('\t\t\t\tASSETCATALOG_COMPILER_APPICON_NAME = AppIcon;')
    w('\t\t\t\tASSETCATALOG_COMPILER_GLOBAL_ACCENT_COLOR_NAME = AccentColor;')
    w('\t\t\t\tCODE_SIGN_STYLE = Automatic;')
    w('\t\t\t\tCURRENT_PROJECT_VERSION = 1;')
    w('\t\t\t\tGENERATE_INFOPLIST_FILE = YES;')
    w('\t\t\t\tINFOPLIST_KEY_CFBundleDisplayName = "Neuro Plans";')
    w('\t\t\t\tINFOPLIST_KEY_UIApplicationSceneManifest_Generation = YES;')
    w('\t\t\t\tINFOPLIST_KEY_UIApplicationSupportsIndirectInputEvents = YES;')
    w('\t\t\t\tINFOPLIST_KEY_UILaunchScreen_Generation = YES;')
    w('\t\t\t\tINFOPLIST_KEY_UISupportedInterfaceOrientations = UIInterfaceOrientationPortrait;')
    w('\t\t\t\t"INFOPLIST_KEY_UISupportedInterfaceOrientations_iPad" = "UIInterfaceOrientationPortrait UIInterfaceOrientationPortraitUpsideDown UIInterfaceOrientationLandscapeLeft UIInterfaceOrientationLandscapeRight";')
    w('\t\t\t\tMARKETING_VERSION = 1.0.0;')
    w('\t\t\t\tPRODUCT_BUNDLE_IDENTIFIER = com.neuroplans.app;')
    w('\t\t\t\tPRODUCT_NAME = "Neuro Plans";')
    w('\t\t\t\tSWIFT_EMIT_LOC_STRINGS = YES;')
    w('\t\t\t\tSWIFT_VERSION = 5.9;')
    w('\t\t\t\tTARGETED_DEVICE_FAMILY = "1,2";')
    w("\t\t\t};")
    w(f'\t\t\tname = Debug;')
    w("\t\t};")

    # Target-level Release
    w(f"\t\t{RELEASE_TARGET} /* Release */ = {{")
    w("\t\t\tisa = XCBuildConfiguration;")
    w("\t\t\tbuildSettings = {")
    w('\t\t\t\tASSETCATALOG_COMPILER_APPICON_NAME = AppIcon;')
    w('\t\t\t\tASSETCATALOG_COMPILER_GLOBAL_ACCENT_COLOR_NAME = AccentColor;')
    w('\t\t\t\tCODE_SIGN_STYLE = Automatic;')
    w('\t\t\t\tCURRENT_PROJECT_VERSION = 1;')
    w('\t\t\t\tGENERATE_INFOPLIST_FILE = YES;')
    w('\t\t\t\tINFOPLIST_KEY_CFBundleDisplayName = "Neuro Plans";')
    w('\t\t\t\tINFOPLIST_KEY_UIApplicationSceneManifest_Generation = YES;')
    w('\t\t\t\tINFOPLIST_KEY_UIApplicationSupportsIndirectInputEvents = YES;')
    w('\t\t\t\tINFOPLIST_KEY_UILaunchScreen_Generation = YES;')
    w('\t\t\t\tINFOPLIST_KEY_UISupportedInterfaceOrientations = UIInterfaceOrientationPortrait;')
    w('\t\t\t\t"INFOPLIST_KEY_UISupportedInterfaceOrientations_iPad" = "UIInterfaceOrientationPortrait UIInterfaceOrientationPortraitUpsideDown UIInterfaceOrientationLandscapeLeft UIInterfaceOrientationLandscapeRight";')
    w('\t\t\t\tMARKETING_VERSION = 1.0.0;')
    w('\t\t\t\tPRODUCT_BUNDLE_IDENTIFIER = com.neuroplans.app;')
    w('\t\t\t\tPRODUCT_NAME = "Neuro Plans";')
    w('\t\t\t\tSWIFT_EMIT_LOC_STRINGS = YES;')
    w('\t\t\t\tSWIFT_VERSION = 5.9;')
    w('\t\t\t\tTARGETED_DEVICE_FAMILY = "1,2";')
    w("\t\t\t};")
    w(f'\t\t\tname = Release;')
    w("\t\t};")

    w("/* End XCBuildConfiguration section */")
    w()

    # --- XCConfigurationList ---
    w("/* Begin XCConfigurationList section */")

    w(f'\t\t{CONFIG_LIST_PROJ} /* Build configuration list for PBXProject "NeuroPlans" */ = {{')
    w("\t\t\tisa = XCConfigurationList;")
    w("\t\t\tbuildConfigurations = (")
    w(f"\t\t\t\t{DEBUG_PROJ} /* Debug */,")
    w(f"\t\t\t\t{RELEASE_PROJ} /* Release */,")
    w("\t\t\t);")
    w("\t\t\tdefaultConfigurationIsVisible = 0;")
    w('\t\t\tdefaultConfigurationName = Release;')
    w("\t\t};")

    w(f'\t\t{CONFIG_LIST_TARGET} /* Build configuration list for PBXNativeTarget "NeuroPlans" */ = {{')
    w("\t\t\tisa = XCConfigurationList;")
    w("\t\t\tbuildConfigurations = (")
    w(f"\t\t\t\t{DEBUG_TARGET} /* Debug */,")
    w(f"\t\t\t\t{RELEASE_TARGET} /* Release */,")
    w("\t\t\t);")
    w("\t\t\tdefaultConfigurationIsVisible = 0;")
    w('\t\t\tdefaultConfigurationName = Release;')
    w("\t\t};")

    w("/* End XCConfigurationList section */")
    w()

    w("\t};")
    w(f"\trootObject = {PROJECT_ID} /* Project object */;")
    w("}")

    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    proj_dir = os.path.join(repo_root, "ios", "NeuroPlans", "NeuroPlans.xcodeproj")
    os.makedirs(proj_dir, exist_ok=True)

    pbxproj_path = os.path.join(proj_dir, "project.pbxproj")
    content = generate_pbxproj()

    with open(pbxproj_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Generated {pbxproj_path}")
    print(f"  {len(SWIFT_FILES)} Swift source files")
    print(f"  {len(RESOURCE_FILES)} resource files")
    print(f"  Target: iOS 17.0, Swift 5.9")
    print(f"\nOpen in Xcode:")
    print(f"  open ios/NeuroPlans/NeuroPlans.xcodeproj")


if __name__ == "__main__":
    main()
