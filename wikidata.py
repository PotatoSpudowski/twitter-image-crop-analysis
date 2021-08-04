from qwikidata.sparql import (get_subclasses_of_item,
                              return_sparql_query_results)
import json 

sparql_query = """
SELECT ?item ?Library_of_Congress_authority_ID ?human ?humanLabel WHERE {
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
  OPTIONAL { ?item wdt:P244 ?Library_of_Congress_authority_ID. }
  ?human wdt:P31 wd:Q5.
}
LIMIT 1000
"""
res = return_sparql_query_results(sparql_query)

with open("out.json", "w") as outfile: 
    json.dump(res, outfile)