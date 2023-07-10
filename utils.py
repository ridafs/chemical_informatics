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
                }
                }
            }
            }
        }
        }
    }
    }
    """.replace("disease_id",disease_id)
    return query_string
