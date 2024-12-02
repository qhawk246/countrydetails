#from Countrydetails import country
import country
import countries

country = country.country_details('India')
print(country.population()) 
print(country.native_name())
print(country.latlng)
print(country.languages())
print(country.capital_latlng())   
print(country.flag())
print(country.demonym())
print(country.currency())    
print(country.independence())
print(country.capital())
print(country.calling_codes())
print(country.borders())    
print(country.area()) 
print(country.alt_spellings()) 
print(country.iso())

#Test regions
country_all = countries.all_countries()
print(country_all.regions())