import requests
import json
def get_disease_query(disease_id):
    # Build query string to get target information as well as count
    query_string = """
    query KnownDrugs {
    disease(efoId: "disease_id") {
        id
        name
            associatedTargets (page: {size: 3, index: 0}) {
        rows{
            score
            target{
            id
            approvedName
            approvedSymbol
            knownDrugs{
                rows{
                drug{
                    name
                    id
                }}
            }}
        }}
    }}
    """.replace("disease_id",disease_id)
    return query_string

def get_targets(disease_id):
    query_string = get_disease_query(disease_id)
    # Set variables object of arguments to be passed to endpoint
    variables = {"efoId": disease_id}

    # Set base URL of GraphQL API endpoint
    base_url = "https://api.platform.opentargets.org/api/v4/graphql"

    # Perform POST request and check status code of response
    r = requests.post(base_url, json={"query": query_string, "variables": variables})

    #Transform API response from JSON into Python dictionary and print in console
    api_response = json.loads(r.text)
    return api_response
