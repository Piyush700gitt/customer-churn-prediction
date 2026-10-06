def calculate_total_services(
    phone_service,
    multiple_lines,
    online_security,
    online_backup,
    device_protection,
    tech_support,
    streaming_tv,
    streaming_movies
):
    return sum([
        phone_service == "Yes",
        multiple_lines == "Yes",
        online_security == "Yes",
        online_backup == "Yes",
        device_protection == "Yes",
        tech_support == "Yes",
        streaming_tv == "Yes",
        streaming_movies == "Yes"
    ])


def get_tenure_group(tenure):

    if tenure <= 12:
        return "New"

    elif tenure <= 24:
        return "Early"

    elif tenure <= 48:
        return "Medium"

    else:
        return "Long-term"


def get_risk_level(probability):

    if probability < 0.30:
        return "Low Risk"

    elif probability < 0.60:
        return "Medium Risk"

    else:
        return "High Risk"