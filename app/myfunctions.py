# functions useful for different back-end/front-end purposes

import requests


class Amiibo_all():
    url = "https://www.amiiboapi.com/api/amiibo/"  

    def request_data(self):
        """
        returns all amiibos as a list from i=0 to i=838
        """
        response = requests.get(self.url)
        data = response.json()
        if not response.ok:
            print("error fetching url")
        data = data["amiibo"]
        return data

# there are 839 different products in the api catalog
class Amiibo():
    """
    Help: instanciate class with a product number arg between 1-839. 
    Use methods: get_id, name, game_series, video_game, img_url, release [US release date] to return information about the product.
    """
    url = "https://www.amiiboapi.com/api/amiibo/"    

    def __init__(self, iteration):
        self.iter = iteration - 1

    def dateTransform(self, string):
        months = {"01": "january", "02": "february", "03": "march", "04": "april", "05": "may" , "06": "june", "07": "july", "08": "august", "09": "september", "10": "october", "11": "november", "12": "december"}
        date = string.split("-")
        year = date[0]
        month = [v for k,v in months.items() if k == date[1]][0]
        day = date[2]
        if day[0] == "0":
            day = day[1]
        if len(day) == 1:
            if day == "1":
                day += "st"
            elif day == "2":
                day += "nd"
            elif day == "3":
                day += "rd"
            else:
                day += "th"
        else:
            if day[0] != "1":
                if day[1] == "1":
                    day += "st"
                elif day[1] == "2":
                    day += "nd"
            else:
                day += "th"
        return " ".join([day, month.title(), year])

    def request_data(self):
        """
        returns amiibos in list of 839 objects
        """
        response = requests.get(self.url)
        data = response.json()
        if not response.ok:
            print("error fetching url")
        if self.iter >= 0 and self.iter <= 839:
            data = data["amiibo"][self.iter]
            return data
        else:
            return None
    
    def get_id(self):
        data = self.request_data()
        amiibo_id = data["tail"]
        return amiibo_id

    def name(self):
        data = self.request_data()
        amiibo_name = data["name"]
        return amiibo_name

    def game_series(self):
        data = self.request_data()
        amiibo_game_series = data["gameSeries"]
        return amiibo_game_series

    def video_game(self):
        data = self.request_data()
        amiibo_video_game = data["amiiboSeries"]
        return amiibo_video_game

    def img_url(self):
        data = self.request_data()
        amiibo_image = data["image"]
        return amiibo_image

    def release(self):
        data = self.request_data()
        amiibo_release_date_US = data["release"]["na"]
        amiibo_release_date = self.dateTransform(amiibo_release_date_US)
        return amiibo_release_date
        
    def details(self):
        """
        Returns dict --> keys: tail_id, iter (index), page (which group of 12 the product falls into), name, game_series, video_game, img_url, release, release_f2 (release date in full text format)
        """
        data = self.request_data()
        if data:
            det_dict = {}
            det_dict["tail_id"] = data["tail"]
            det_dict["iter"] = self.iter
            det_dict["page"] = self.iter // 12 + 1
            det_dict["name"] = data["name"]
            det_dict["game_series"] = data["gameSeries"]
            det_dict["video_game"] = data["amiiboSeries"]
            det_dict["img_url"] = data["image"]
            det_dict["release"] = data["release"]["na"]
            if det_dict["release"]:
                det_dict["release_f2"] = self.dateTransform(data["release"]["na"])
            else:
                det_dict["release_f2"] = None
            return det_dict
        else:
            return None

    
### examples of pulling info with the Amiibo class
### first product
# product1 = Amiibo(1)
# print(product1.details())

### last product
# product839 = Amiibo(839)
# print(product839.release())



