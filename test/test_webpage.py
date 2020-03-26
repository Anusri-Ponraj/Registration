from bs4 import BeautifulSoup
import pytest
import pickle
import requests

class TestWebpage:
    @pytest.fixture(autouse=True)
    def get_soup(self):
        index_page = requests.get("http://localhost:8000/index.html")
        soup_index = BeautifulSoup(index_page.content, 'html.parser')
        self._index = soup_index
        
    # testing index.html
    def test_indexpage(self):
        assert self._index.find_all('form')
        assert self._index.body.h1.string=='Registration Form'
        site = self._index.find('form')
        assert self._index.find('form')
        site1 = site.find_all('input')
        count = 0
        for input in site1:
            count +=1
        assert count==6
        assert self._index.find('datalist')
        site2=site.find_all('datalist')
        site3=self._index.find_all('option')
        count = 0
        for option in site3:
            count +=1
        assert count==5
        assert self._index.find_all('input', {'type': 'text'})
        assert self._index.find_all('input', {'type': 'date'})
        assert self._index.find_all('input', {'type': 'email'})
        assert self._index.find_all('input', {'type': 'tel'})
        assert self._index.find_all('input', {'type': 'url'})
     
      