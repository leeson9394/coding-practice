def fetch_page(page):
    """
    Return the page of results and the next page. Pages are 0 indexed.
    returns:
        {
            "results": [...],
            "next_page": 3
        }
    """
    dictionary = {
            "results": "[...]",
            "next_page": 3
        }
    # pass
    return dictionary


# fetch_page(0)    ->.  5 results + next_page:1
# fetch_page(1).   ->.  5 resutls + next_page:2
# fetch_page(2).   ->  3 results + next_page:3
# fetch_page(3).   -> 0 results + next_page:0



def fetch(n):
    page = 0  # start from page 0
    res = [] 
    result_counter = 0 
    
    # if n - result_counter > 0:
    #     page_result = fetch_page(page) 
    #     next_page = page_result["next_page"]
    #     res.append(page_result["results"])
    #     result_counter += len(page_result["results"])
    #     fetch_page(next_page)  

    while result_counter < n:
        page_dict = fetch_page(page) 
        page = page_dict["next_page"]
        res.append(page_dict["results"])
        result_counter += len(page_dict["results"])
    return res


# fetch(6).  -> the first 6 results
# fetch(2).  -> results 7-8
# fetch(4).  -> results 9-12
# fetch(10). -> results 13
# fetch(4)   -> 0 results