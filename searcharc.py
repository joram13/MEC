



import pandas as pd
import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import math
from selenium.webdriver.common.action_chains import ActionChains



# Reading an excel file using Python






def get_distance(n1, e1, n2, e2):
    distx = abs(n1-n2) * 111111
    disty = abs(e1-e2) * 71430
    dist = math.sqrt((distx**2) + (disty**2))
    return dist

def bf(long, lat):
    start = time.time()

    driver1 = webdriver.Chrome(ChromeDriverManager().install())
    #driver2 = webdriver.Chrome(ChromeDriverManager().install())
    #driver3 = webdriver.Chrome(ChromeDriverManager().install())
    #driver4 = webdriver.Chrome(ChromeDriverManager().install())
    #driver5 = webdriver.Chrome(ChromeDriverManager().install())
    #driver6 = webdriver.Chrome(ChromeDriverManager().install())
    #driver7 = webdriver.Chrome(ChromeDriverManager().install())
    #driver8 = webdriver.Chrome(ChromeDriverManager().install())
    #driver9 = webdriver.Chrome(ChromeDriverManager().install())
    #driver10 = webdriver.Chrome(ChromeDriverManager().install())
    #driver11 = webdriver.Chrome(ChromeDriverManager().install())
    #driver12 = webdriver.Chrome(ChromeDriverManager().install())
    #driver13 = webdriver.Chrome(ChromeDriverManager().install())
    #driver14 = webdriver.Chrome(ChromeDriverManager().install())
    #driver15 = webdriver.Chrome(ChromeDriverManager().install())
    #driver16 = webdriver.Chrome(ChromeDriverManager().install())
    #driver17 = webdriver.Chrome(ChromeDriverManager().install())
    #driver18 = webdriver.Chrome(ChromeDriverManager().install())
    #driver19 = webdriver.Chrome(ChromeDriverManager().install())
    #driver20 = webdriver.Chrome(ChromeDriverManager().install())
    #driver21 = webdriver.Chrome(ChromeDriverManager().install())
    drivers = [driver1]#, driver2, driver3]#, driver4, driver5, driver6, driver7, driver8, driver9, driver10, driver11, driver12, driver13]#, driver14, driver15, driver16, driver17, driver18, driver19, driver20, driver21]





    for i in drivers:
        i.set_window_size(1920, 1080)



    for i in drivers:
        i.get("https://pecms.maps.arcgis.com/home/webmap/viewer.html?webmap=5c919617229645e8a4c413b1ee9ea87f")

    #document.querySelector("#user_username")
    #document.querySelector("#user_password")
    #document.querySelector("#signIn")
    #document.querySelector("#geocoder_input")
    #document.querySelector("#dijit_form_Button_2")
    #document.querySelector("#Adressen_Sachsen_4040_checkbox")
    #document.querySelector("#map_root > div.blueTheme.esriPopup.esriPopupVisible")
    #document.querySelector("#map_root > div.blueTheme.esriPopup.esriPopupVisible > div.outerPointer.left")
    #document.querySelector("#esri_dijit__PopupRenderer_54 > div.mainSection > div:nth-child(3) > table > tr:nth-child(4) > td.attrValue")
    #document.querySelector("#esri_dijit__PopupRenderer_10 > div.mainSection > div:nth-child(3) > table > tr:nth-child(3) > td.attrValue")
    #document.querySelector("#esri_dijit__PopupRenderer_0 > div.mainSection > div:nth-child(3) > table > tr:nth-child(4) > td.attrValue")
    #document.querySelector("#Leipzig_GIS2_3066_checkbox")
    #document.querySelector("#Vonovia\\ Leipzig_5415_checkbox")
    #document.querySelector("#KiTa_in_Leipzig_7777_checkbox")
    #document.querySelector("#Fam_Bildg_Soz_8920_checkbox")
    #document.querySelector("#WirWis_TS_mobil_1586_checkbox")
    #
    time.sleep(10)

    for i in drivers:
        i.execute_script("return document.querySelector('#user_username')").send_keys("PEC_Management_Solutions")
        i.execute_script("return document.querySelector('#user_password')").send_keys("PECMS2021")
        i.execute_script("return document.querySelector('#signIn')").click()
        time.sleep(30)
        i.execute_script("return document.querySelector('#dijit_form_Button_2')").click()
        time.sleep(5)
        i.execute_script("return document.querySelector('#Adressen_Sachsen_4040_checkbox')").click()
        time.sleep(1)
        i.execute_script("return document.querySelector('#Leipzig_GIS2_3066_checkbox')").click()
        time.sleep(1)
        #i.execute_script("return document.querySelector('Vonovia\\ Leipzig_5415_checkbox')").click()
        time.sleep(1)
        i.execute_script("return document.querySelector('#KiTa_in_Leipzig_7777_checkbox')").click()
        time.sleep(1)
        i.execute_script("return document.querySelector('#Fam_Bildg_Soz_8920_checkbox')").click()
        time.sleep(1)
        i.execute_script("return document.querySelector('#WirWis_TS_mobil_1586_checkbox')").click()
        time.sleep(5)

    lineh = []
    linei = []
    for yy in range(len(long)):
        for i in drivers:
            if yy != 0:

                i.execute_script("return document.querySelector('#geocoder > div > div.searchExpandContainer > div > div.searchInputGroup > div.searchClear')").click()
                time.sleep(1)
            i.execute_script("return document.querySelector('#geocoder_input')").send_keys(str(lat[yy])+","+str(long[yy]))
            i.execute_script("return document.querySelector('#geocoder_input')").send_keys(Keys.ENTER)
            time.sleep(3)
            action = webdriver.ActionChains(i)
            action.move_to_element(i.execute_script("return document.querySelector('#map_root > div.blueTheme.esriPopup.esriPopupVisible')")).perform()
            action.click().perform()
            time.sleep(5)
            #print(yy)
            #document.querySelector("#esri_dijit__PopupRenderer_93 > div.mainSection > div:nth-child(3) > table > tr:nth-child(3) > td.attrValue"
            tt = yy
            if yy > 91:
                tt += 1
            print(tt)
            a = i.execute_script(f"return document.querySelector('#esri_dijit__PopupRenderer_{str(yy)} > div.mainSection > div:nth-child(3) > table > tr:nth-child(4) > td.attrValue')").text
            b = i.execute_script(f"return document.querySelector('#esri_dijit__PopupRenderer_{str(yy)} > div.mainSection > div:nth-child(3) > table > tr:nth-child(3) > td.attrValue')").text
            print(a)
            print(b)
            lineh.append(a)
            linei.append(b)
    print(lineh)
    print(linei)

    #time.sleep(100)



long = [51.334846, 51.341981, 51.341215, 51.337521, 51.336794, 51.337561, 51.337897, 51.339096, 51.343801, 51.337672, 51.336998, 51.340623, 51.34107, 51.339548, 51.341916, 51.342856, 51.340258, 51.338162, 51.339355, 51.342632, 51.342709, 51.330408, 51.341491, 51.3416942, 51.317785, 51.319172, 51.32336, 51.322935, 51.32283, 51.32751, 51.325938, 51.324828, 51.339043, 51.338919, 51.352392, 51.319166, 51.31932, 51.325974, 51.325738, 51.325758, 51.329257, 51.335435, 51.341333, 51.34029, 51.374529, 51.32186, 51.324517, 51.329649, 51.328601, 51.329505, 51.305645, 51.30674, 51.305924, 51.312037, 51.31258, 51.313415, 51.328681, 51.325128, 51.328037, 51.368169, 51.368497, 51.379571, 51.378841, 51.387297, 51.394381, 51.40236, 51.299839, 51.300999, 51.301456, 51.309136, 51.247473, 51.249912, 51.373289, 51.373232, 51.321346, 51.320293, 51.322841, 51.323492, 51.362047, 51.363587, 51.373648, 51.371693, 51.380968, 51.380258, 51.330825, 51.33085, 51.404227, 51.285847, 51.288184, 51.302299, 51.301905, 51.314226, 51.313868, 51.36629, 51.378408, 51.379451, 51.380299, 51.40865, 51.336106, 51.335703, 51.33585, 51.337781, 51.295604, 51.29675, 51.305802, 51.318689, 5131934.0, 51.327621, 51.340232, 51.341915, 51.349708, 51.349769, 51.361709, 51.369579, 51.37898, 51.370613, 51.37125, 51.289925, 51.29022, 51.301662, 51.316759, 51.324442, 51.325761, 51.3256, 51.364193, 51.36475, 51.36476, 51.369651, 51.368643, 51.368804, 51.345727, 51.346233, 51.34679, 5134571.0, 51.356926, 51.357974, 51.363783, 51.362397, 51.374897, 51.375036, 51.37546, 51.294461, 51.29381, 51.30694, 51.306866, 51.360818, 51.360543, 51.336886, 51.339755, 51.366204, 51.37198, 51.372638, 51.380498, 51.280112, 51.283615, 51.346568, 51.347503, 51.34729, 51.34734, 51.339448, 51.33945, 51.340934, 51.341971, 51.356917, 51.35704, 51.361824, 51.36203, 51.363158, 51.369321, 51.36984, 51.36914, 51.36862, 51.374735, 51.37566, 51.320024, 51.319538, 51.327317, 51.327739, 51.32105, 51.323663, 51.318544, 51.345953, 51.346481, 51.320024, 51.319538, 51.327317, 51.327739, 51.32105, 51.323663, 51.318544, 51.345953, 51.346481, 51.344673, 51.344221, 51.34476]
lat = [12.371082, 12.368443, 12.367771, 12.371567, 12.37074, 12.374446, 12.368611, 12.36912, 12.372592, 12.375545, 12.37594, 12.377892, 12.378713, 12.377993, 12.377212, 12.376405, 12.383634, 12.382303, 12.383474, 12.38095, 12.379605, 12.316062, 12.324278, 12.3229113, 12.327374, 12.327797, 12.325351, 12.324751, 12.326729, 12.323088, 12.315911, 12.315354, 12.324454, 12.322797, 12.32268, 12.327795, 12.331454, 12.335625, 12.336148, 12.334941, 12.329918, 12.330741, 12.330682, 12.332215, 12.322146, 12.341069, 12.3388, 12.344584, 12.344295, 12.341798, 12.374074, 12.377243, 12.376031, 12.373605, 12.373719, 12.374769, 12.382883, 12.388285, 12.383907, 12.390806, 12.386527, 12.387505, 12.387735, 12.390414, 12.394951, 12.389621, 12.395889, 12.395621, 12.393931, 12.393861, 12.266905, 12.264842, 12.336187, 12.336734, 12.394641, 12.395604, 12.39186, 12.391012, 12.403436, 12.404863, 12.40734, 12.403222, 12.403434, 12.406277, 12.338978, 12.340022, 12.406899, 12.395647, 12.393646, 12.418692, 12.417879, 12.417565, 12.419664, 12.423493, 12.418873, 12.419362, 12.41925, 12.42694, 12.33829, 12.335744, 12.33522, 12.339358, 12.428444, 12.428388, 12.426198, 12.429813, 1242735.0, 12.433661, 12.432219, 12.435496, 12.433179, 12.431105, 12.430025, 12.337562, 12.434803, 12.341168, 12.33886, 12.44513, 12.45133, 12.439588, 12.448217, 12.453822, 12.450638, 12.45214, 12.350363, 1234987.0, 12.34949, 12.347347, 12.348474, 12.350302, 12.449712, 12.45411, 12.45088, 12.45256, 12.461735, 12.457788, 12.453724, 12.446954, 12.352608, 12.348913, 12.3456, 12.452422, 12.455769, 12.459352, 12.459787, 12.356036, 12.355618, 12.477731, 12.483353, 12.353793, 12.358717, 12.460781, 12.359108, 12.469147, 12.473383, 12.352233, 12.353043, 12.35368, 12.35242, 12.376138, 12.3769, 12.36028, 12.359571, 12.363723, 12.36469, 12.360999, 12.361047, 12.361818, 12.365249, 12.364412, 12.36451, 12.36284, 12.362491, 12.360217, 12.366615, 12.367136, 12.369017, 12.369473, 12.368603, 12.473136, 12.47399, 12.486341, 12.485281, 12.366615, 12.367136, 12.369017, 12.369473, 12.368603, 12.473136, 12.47399, 12.486341, 12.485281, 12.366441, 12.368681, 12.36659]
bf(long, lat)
