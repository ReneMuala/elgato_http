import sys
from termcolor import colored

sys.path.append("lib/")

from elgato import Test

common_headers = {
    "token": "1234",
}

def main():
    tests = [
        Test(
            name="test-search",
            method="get",
            uri="google.com/search/q=elgato",
            headers=common_headers,
            expects=[200],
        ),
        Test(
            name="test-404",
            method="get",
            uri="google.com/404",
            headers=common_headers,
            expects=[404],
        ),
    ]


    unperfomed_tests_case = False

    for test in tests:
        test.perform()
        _, passed = test.get_test_status()
        if not passed:
            if test.response != None:
                print(f"body: {test.response.content}")
            else:
                unperfomed_tests_case = True
    if unperfomed_tests_case:
        print_hint("check the your internet connection and the request's uri", scope="Unperfomed")
 
if __name__ == "__main__":
    main()

def print_hint(hint:str, scope:str|None=None):
    if scope is not None:
        print(f"Hint({scope}): ", end="")
    else:
        print("Hint: ", end="")

    print(colored(hint,"yellow"))