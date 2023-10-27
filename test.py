from operator import attrgetter
import pycountry


def getCountries():
    """['ae' 'ar' 'at' 'au' 'be' 'bg' 'br' 'ca' 'ch' 'cn' 'co' 'cu' 'cz' 'de' 'eg' 'fr' 'gb' 'gr' 'hk' 'hu' 'id' 'ie' 'il' 'in' 'it' 'jp' 'kr' 'lt' 'lv' 'ma' 'mx' 'my' 'ng' 'nl' 'no' 'nz' 'ph' 'pl' 'pt' 'ro' 'rs' 'ru' 'sa' 'se' 'sg' 'si' 'sk' 'th' 'tr' 'tw' 'ua' 'us' 've' 'za']"""
    # fetch only above states
    selected_countries = [
        country
        for country in list(
            map(attrgetter("alpha_2", "name"), list(pycountry.countries))
        )
        if country[0].lower()
        in [
            "ae",
            "ar",
            "at",
            "au",
            "be",
            "bg",
            "br",
            "ca",
            "ch",
            "cn",
            "co",
            "cu",
            "cz",
            "de",
            "eg",
            "fr",
            "gb",
            "gr",
            "hk",
            "hu",
            "id",
            "ie",
            "il",
            "in",
            "it",
            "jp",
            "kr",
            "lt",
            "lv",
            "ma",
            "mx",
            "my",
            "ng",
            "nl",
            "no",
            "nz",
            "ph",
            "pl",
            "pt",
            "ro",
            "rs",
            "ru",
            "sa",
            "se",
            "sg",
            "si",
            "sk",
            "th",
            "tr",
            "tw",
            "ua",
            "us",
            "ve",
            "za",
        ]
    ]
    return selected_countries


all_countries = getCountries()
print(all_countries)
