import listfunctionsexercise, pytest

@pytest.mark.parametrize("original, copy", [
    ([1,2,3], [1,2,3]),
    (["a","b","c"],["a","b","c"]),
    ([True,False],[True,False])
])

def test_clone_a_list(original, copy):
    assert listfunctionsexercise.clone_a_list(original) == copy
    
@pytest.mark.parametrize("n, arraylist, occurrences", [
    (3,[1,3,3,5,5,5], 2),
    ("a",["a","b","a","a",1,1,3,True,False],3)
])

def test_number_of_occurrences_in_a_list(n, arraylist, occurrences):
    assert listfunctionsexercise.number_of_occurrences_in_a_list(n, arraylist) == occurrences
    
@pytest.mark.parametrize("arraylist, output", [
    ([(1,2),("m",3),(),("o","k")], [(1,2),("m",3),("o","k")]), 
    ([(),("mikyle"),(),(),(8,"hey",True)], [("mikyle"),(8,"hey",True)])
])

def test_remove_empty_tuples_from_list(arraylist, output):
    assert listfunctionsexercise.remove_empty_tuples_from_list(arraylist) == output
    
@pytest.mark.parametrize("arraylist, duplicates", [
    ([1,3,3,5,5,5], [3,5]),
    (["a","b","c","a",1,1,3,True,False],["a",1])
])

def test_remove_duplicates_from_list(arraylist, duplicates):
    assert listfunctionsexercise.remove_duplicates_from_list(arraylist) == duplicates
    