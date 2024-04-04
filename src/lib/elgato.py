import requests
from termcolor import colored
from json import JSONEncoder

json_encoder = JSONEncoder()

class Test:
    def __init__(self, 
    name: str, 
    uri:str,
    method : str = "post",
    headers: dict[str, str] = {},
    body: any = {},
    expects : list[int] = [],
    ):
        self.method = method
        self.name = name
        self.headers = headers
        self.uri = uri
        self.body = body
        self.expects = expects
        self.response : requests.Response | None = None
    
    def get_test_id(self)->str:
        return f"{self.name} : {self.uri}"
    
    def get_test_status(self)->tuple[
        str, # status str
        bool # status
        ]:
        status : bool = False
        status_str : str = "Unperformed"
        if(self.response != None):
            if( self.expects.count(self.response.status_code) >= 1):
                status_str = "Passed"
                status = True
            else:
                status_str = f"Failed width status-code: {self.response.status_code}, expected-status-codes: {self.expects}"
        return [status_str, status]

    def add_headers(self, headers:dict[str, str]):
        self.headers.update(headers)

    def add_expects(self, expects:list[int]):
        self.expects.append(expects)

    def set_uri(self, uri: str):
        self.uri = uri

    def set_body(self, body):
        if(type(body) is type(str)):
            self.body = body
        else:
            self.body = json_encoder.encode(o=body)
    
    def perform(self):
        print(self.get_test_id())
        try:
            self.response = requests.request(
                method=self.method,
                url=self.uri, 
                json=self.body,
                headers=self.headers
            )
        except:
            pass
        status_str, passed = self.get_test_status()
        print("status: ", end="")
        if passed:
            print(colored(f"{status_str}", "green"))
        else:
            print(colored(f"{status_str}", "red"))

    def print(self):
        print(self.get_test_id())
        print(self.headers)
        print(self.body)