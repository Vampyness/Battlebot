# scout_analyzer.py

def analyze_scout_report(report_text):
    suggestions = []
    report_text = report_text.lower()

    if "rider" in report_text and "barbarian" in report_text:
        suggestions.append("Enemy using Rider + Barb mix. Try Guardians + Hunters.")
    if "3x rider" in report_text or report_text.count("rider") >= 3:
        suggestions.append("Heavy Rider stack. Avoid Hunters. Use Barb frontlines.")
    if "behemoth" in report_text:
        suggestions.append("Enemy includes Behemoth. Consider using Riders to intercept.")
    if "low tier" in report_text or "t7" in report_text or "t6" in report_text:
        suggestions.append("Target has layered low tiers. Overwhelm with burst Riders or Hunters.")
    if "2x barb" in report_text:
        suggestions.append("2x Barb detected. Use ranged-heavy setup to pierce defense.")

    if not suggestions:
        suggestions.append("Standard layout. Use mixed T10+ with one counter layer based on beast type.")

    return suggestions
