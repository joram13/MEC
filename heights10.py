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


def get_starting_points(n, e, ra, f,ff):
    t = 5
    if ra == 100:
        s = 4
    if ra == 150:
        s = 6
    if ra == 200:
        s = 8
    if ra == 300:
        s = 12

    for i in range((t*s)+1):
        c22 = t*i
        #print(c22)
        c11 = math.sqrt((ra**2) - (c22**2))
        c1 = c11 * 0.000009
        c2 = c22 * 0.000014
        #print(c1, c2)
        if i == 0:
            cur1 = [round(n+c1, 6), round(e+c2, 6)]
            f.append(cur1)
            ff.append(cur1)
            #l[str(cur1[0]) + "," + str(cur1[1])] = [cur1]

        else:
            cur1 = [round(n+c1, 6), round(e-c2, 6)]
            cur2 = [round(n+c1, 6), round(e+c2, 6)]
            f.append(cur1)
            f.append(cur2)
            ff.append(cur1)
            ff.append(cur2)
            #l[str(cur1[0]) + "," + str(cur1[1])] = [cur1]
            #l[str(cur1[0]) + "," + str(cur1[1])] = [cur1]

def get_distance(n1, e1, n2, e2):
    distx = abs(n1-n2) * 111111
    disty = abs(e1-e2) * 71430
    dist = math.sqrt((distx**2) + (disty**2))
    return dist

def bf(coordinates, radius):
    start = time.time()

    driver1 = webdriver.Chrome(ChromeDriverManager().install())
    driver2 = webdriver.Chrome(ChromeDriverManager().install())
    driver3 = webdriver.Chrome(ChromeDriverManager().install())
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
    drivers = [driver1, driver2, driver3]#, driver4, driver5, driver6, driver7, driver8, driver9, driver10, driver11, driver12, driver13]#, driver14, driver15, driver16, driver17, driver18, driver19, driver20, driver21]



    dict = []
    listofpoints = []
    startpoints1 = []
    startpoints2 = []

    for i in range(len(coordinates)):
        dict.append({})
        listofpoints.append([])
        startpoints1.append([])
        startpoints2.append([])




    for i in drivers:
        i.get("https://earth.google.com/web/")
        #time.sleep(30)
    time.sleep(30)

    for i in drivers:
        i.execute_script("return document.querySelector('body > earth-app').shadowRoot.querySelector('#toolbar').shadowRoot.querySelector('#menu')").click()
    time.sleep(1)

    for i in drivers:
        i.execute_script("return document.querySelector('body > earth-app').shadowRoot.querySelector('#menu').shadowRoot.querySelector('#settings-button')").click()
    time.sleep(2)

    for i in drivers:
        i.execute_script("return document.querySelector('#settings-dialog').shadowRoot.querySelector('#scrollable > earth-collapsible-panel:nth-child(1)').shadowRoot.querySelector('#expando')").click()
    time.sleep(1)

    for i in drivers:
        i.execute_script("return document.querySelector('#settings-dialog').shadowRoot.querySelector('#scrollable > earth-collapsible-panel:nth-child(2)').shadowRoot.querySelector('#expando')").click()
    time.sleep(1)

    for i in drivers:
        i.execute_script("return document.querySelector('#settings-dialog').shadowRoot.querySelector('#lat-lng-formats-dropdown').shadowRoot.querySelector('#field > earth-gm2-icon-button')").click()
    time.sleep(1)

    for i in drivers:
        i.execute_script("return document.querySelector('#settings-dialog').shadowRoot.querySelector('#lat-lng-formatting > earth-gm2-menu-item:nth-child(3)')").click()
    time.sleep(1)

    for i in drivers:
        i.execute_script("return document.querySelector('#settings-dialog').shadowRoot.querySelector('#scrollable > earth-collapsible-panel:nth-child(3)').shadowRoot.querySelector('#expando')").click()
    time.sleep(1)

    for i in drivers:
        i.execute_script("return document.querySelector('#settings-dialog').shadowRoot.querySelector('#scrollable > earth-collapsible-panel:nth-child(4)').shadowRoot.querySelector('#expando')").click()
    time.sleep(1)
    for i in drivers:
        i.execute_script("return document.querySelector('#settings-dialog').shadowRoot.querySelector('#scrollable > earth-collapsible-panel:nth-child(1)').shadowRoot.querySelector('#expando')").click()
    time.sleep(1)

    for i in drivers:
        i.execute_script("return document.querySelector('#settings-dialog').shadowRoot.querySelector('#fly-end-view-animation-dropdown').shadowRoot.querySelector('#field > earth-gm2-icon-button')").click()
    time.sleep(1)

    for i in drivers:
        i.execute_script("return document.querySelector('#settings-dialog').shadowRoot.querySelector('#fly-end-view-animation > earth-gm2-menu-item:nth-child(3)')").click()
    time.sleep(1)

    for i in drivers:
        ActionChains(i).drag_and_drop_by_offset(i.execute_script("return document.querySelector('#settings-dialog').shadowRoot.querySelector('#fly-speed-slider').shadowRoot.querySelector('#sliderBar')"), 300, 0).release().perform()
    time.sleep(1)

    for i in drivers:
        i.execute_script("return document.querySelector('#settings-dialog').shadowRoot.querySelector('#save-button')").click()
    time.sleep(1)

    for i in drivers:
        i.execute_script("return document.querySelector('body > earth-app').shadowRoot.querySelector('#toolbar').shadowRoot.querySelector('#menu')").click()
    time.sleep(1)

    for i in drivers:
        i.execute_script("return document.querySelector('body > earth-app').shadowRoot.querySelector('#menu').shadowRoot.querySelector('#map-style-button')").click()
    time.sleep(1)

    for i in drivers:
        i.execute_script("return document.querySelector('body > earth-app').shadowRoot.querySelector('#drawer-container').shadowRoot.querySelector('#mapstyle').shadowRoot.querySelector('#header-layout > aside > paper-radio-group > earth-radio-card:nth-child(1)')").click()
    time.sleep(1)

    for i in drivers:
        i.execute_script("return document.querySelector('body > earth-app').shadowRoot.querySelector('#drawer-container').shadowRoot.querySelector('#mapstyle').shadowRoot.querySelector('#back-button')").click()
    time.sleep(1)


    for qq in range(len(coordinates)):
        print(coordinates[qq][0], coordinates[qq][1], radius[qq], startpoints1[qq], startpoints2[qq])

        get_starting_points(coordinates[qq][0], coordinates[qq][1], radius[qq], startpoints1[qq], startpoints2[qq])
        #sorted_list = sorted(l, key=lambda x: (x[1], x[0]))
        startpoints1[qq] = sorted(startpoints1[qq], key=lambda x: (x[1]))
        ff = []
        for ii in range(len(startpoints1[qq])):

            if ii%2 == 0:
                ff.append(startpoints1[qq][ii])

        startpoints1[qq] = ff
        startpoints2[qq] = ff



        startpoints2[qq] = sorted(startpoints2[qq], key=lambda x: (get_distance(0, 0, x[0], 0)))
        print(startpoints2)
        #print(startpoints1[qq])
        #print(startpoints2[qq])

        for i in drivers:
            i.execute_script("return document.querySelector('body > earth-app').shadowRoot.querySelector('#toolbar').shadowRoot.querySelector('#search')").click()
        #time.sleep(5)

        if qq != 0:
            for i in range(len(drivers)):
                d = drivers[i]
                ttestt = True
                while ttestt:
                    try:
                        d.execute_script("return document.querySelector('body > earth-app').shadowRoot.querySelector('#drawer-container').shadowRoot.querySelector('#search').shadowRoot.querySelector('#omnibox').shadowRoot.querySelector('#clear-button')").click()
                        ttestt = False
                    except:
                        time.sleep(0.5)

        for i in drivers:
            i.execute_script("return document.querySelector('body > earth-app').shadowRoot.querySelector('#drawer-container').shadowRoot.querySelector('#search').shadowRoot.querySelector('#omnibox').shadowRoot.querySelector('#omnibox-input')").send_keys(str(coordinates[qq][0])+","+str(coordinates[qq][1]))
            i.execute_script("return document.querySelector('body > earth-app').shadowRoot.querySelector('#drawer-container').shadowRoot.querySelector('#search').shadowRoot.querySelector('#omnibox').shadowRoot.querySelector('#omnibox-input')").send_keys(Keys.ENTER)
        time.sleep(15)

        for i in drivers:
            i.execute_script("return document.querySelector('body > earth-app').shadowRoot.querySelector('#knowledge-card').shadowRoot.querySelector('#top-card').shadowRoot.querySelector('#close')").click()
        time.sleep(2)

    #count = 0


                #print(d.execute_script("return document.querySelector('earth-app').shadowRoot.querySelector('earth-view-status').shadowRoot.querySelector('span#pointer-elevation')").text[:-1])

        nd1 = [t for t in range(len(drivers))]
        nd2 = [t for t in range(len(drivers))]
        nd4 = [t for t in range(len(drivers))]
        pp = [0 for i in range(len(drivers))]

        nd3 = []

        print("time1", time.time()  - start)
        while len(nd3) < len(drivers):
            print(qq)
            print(len(nd3))
            #print(nd4)
            #print(startpoints2[qq])
            print(len(nd4))
            print(len(startpoints2[qq]))
            print()

            newvar = False
            if len(nd4) > 2 or len(startpoints2[qq]) == len(nd4) and len(startpoints2[qq]) != 0:
                print("first one")
                newvar = True
                for u in range(len(drivers)):
                    if u in nd4:
                        d = drivers[u]
                        #WebDriverWait(d,5).until(EC.visibility_of(d.execute_script("return document.querySelector('body > earth-app').shadowRoot.querySelector('#toolbar').shadowRoot.querySelector('#search')")))
                        d.execute_script("return document.querySelector('body > earth-app').shadowRoot.querySelector('#toolbar').shadowRoot.querySelector('#search')").click()
                #if len(nd4) > 5 and len(nd4) < 13:
                #    time.sleep(3)
                #else:
                #    time.sleep(3)
                ##print("lg1")
                for u in range(len(drivers)):
                    if u in nd4:
                        d = drivers[u]
                    #WebDriverWait(i,5).until(EC.visibility_of(d.execute_script("return document.querySelector('body > earth-app').shadowRoot.querySelector('#drawer-container').shadowRoot.querySelector('#search').shadowRoot.querySelector('#omnibox').shadowRoot.querySelector('#clear-button')")))
                        ttestt = True
                        while ttestt:
                            try:
                                d.execute_script("return document.querySelector('body > earth-app').shadowRoot.querySelector('#drawer-container').shadowRoot.querySelector('#search').shadowRoot.querySelector('#omnibox').shadowRoot.querySelector('#clear-button')").click()
                                ttestt = False
                            except:
                                time.sleep(0.5)
            #time.sleep(3)
                ##print("lg2")
                for u in range(len(drivers)):
                    if u in nd4:
                        d = drivers[u]
                        try:
                            d.execute_script("return document.querySelector('body > earth-app').shadowRoot.querySelector('#drawer-container').shadowRoot.querySelector('#search').shadowRoot.querySelector('#omnibox').shadowRoot.querySelector('#clear-button')").click()
                            time.sleep(0.5)
                        except Exception:
                            pass
                        d.execute_script("return document.querySelector('body > earth-app').shadowRoot.querySelector('#drawer-container').shadowRoot.querySelector('#search').shadowRoot.querySelector('#omnibox').shadowRoot.querySelector('#omnibox-input')").send_keys(str(startpoints2[qq][0][0]) + "," + str(startpoints2[qq][0][1]))
                        startpoints2[qq].remove(startpoints2[qq][0])
                        d.execute_script("return document.querySelector('body > earth-app').shadowRoot.querySelector('#drawer-container').shadowRoot.querySelector('#search').shadowRoot.querySelector('#omnibox').shadowRoot.querySelector('#omnibox-input')").send_keys(Keys.ENTER)

                    #if len(nd4) > 0 and len(nd4) < 13:
                    #    time.sleep(1)
                    #else:
                        #time.sleep(1)


                #time.sleep(3)
                ##print("lg3")
                for u in range(len(drivers)):
                    if u in nd4:
                        d = drivers[u]
                        #WebDriverWait(i,5).until(EC.visibility_of(d.execute_script("return document.querySelector('body > earth-app').shadowRoot.querySelector('#knowledge-card').shadowRoot.querySelector('#top-card').shadowRoot.querySelector('#close')")))
                        ttestt = True
                        while ttestt:
                            try:
                                d.execute_script("return document.querySelector('body > earth-app').shadowRoot.querySelector('#knowledge-card').shadowRoot.querySelector('#top-card').shadowRoot.querySelector('#close')").click()
                                ttestt = False
                            except:
                                time.sleep(0.5)
                        time.sleep(3)


                    #time.sleep(5)
            #time.sleep(3)
                ##print("lg4")
                for y in range(10):
                    for u in range(len(drivers)):
                        if u in nd4:
                    #time.sleep(1)
                            d = drivers[u]
                            try:
                                d.execute_script("return document.querySelector('body > earth-app').shadowRoot.querySelector('#zoom-buttons').shadowRoot.querySelector('#zoom-in')").click()
                            except:
                                #document.querySelector("#expanded-card").shadowRoot.querySelector("#back-button").shadowRoot.querySelector("#icon")
                                d.execute_script("return document.querySelector('#expanded-card').shadowRoot.querySelector('#back-button').shadowRoot.querySelector('#icon')").click()
                                time.sleep(2)
                                d.execute_script("return document.querySelector('body > earth-app').shadowRoot.querySelector('#zoom-buttons').shadowRoot.querySelector('#zoom-in')").click()
                        time.sleep(0.5)
                        if y == 9 and u in nd4:
                           nd4.remove(u)

            ##print("lg5")
            #if len(nd1) > 6 or len(startpoints2[qq]) == len(nd1) and len(nd1) != 0:
            if newvar:
                print("second one here")
                for u in range(len(drivers)):
                    if u in nd1:
                        ##print("nd: 1", u)newvar = Falsenewvar = False
                        d = drivers[u]
                    #print(u)
                    #action.move_by_offset(43, -100).click().perform()


                        action = webdriver.ActionChains(d)
                        #try:
                        action.move_to_element(d.execute_script("return document.querySelector('body > earth-app').shadowRoot.querySelector('#earth-relative-elements > earth-view-status').shadowRoot.querySelector('#percentage-text')")).perform()
                for u in range(len(drivers)):
                    if u in nd1:
                        d = drivers[u]
                        action = webdriver.ActionChains(d)
                        print(u, "click")
                        action.move_by_offset(10, -50).click().perform()
                    #time.sleep(1)
                    #except:
                    #    action.move_by_offset(10, -50).click().perform()
                        nd1.remove(u)
                for u in range(len(drivers)):
                    if u in nd2:
                        ##print("nd: 2", u)#, d.execute_script("return document.querySelector('body > earth-app').shadowRoot.querySelector('#earth-relative-elements > earth-view-status').shadowRoot.querySelector('#pointer-coordinates')").text)
                        d = drivers[u]
                        action = webdriver.ActionChains(d)
                        action.move_to_element(d.execute_script("return document.querySelector('body > earth-app').shadowRoot.querySelector('#earth-relative-elements > earth-view-status').shadowRoot.querySelector('#percentage-text')")).perform()
                        nd2.remove(u)
                ##print("lg0")

            print("time3", time.time()  - start)
            for u in range(len(drivers)):
                if pp[u] != 0:
                    d = drivers[u]
                    n = "0"
                    #while n=="0" or n  == d.execute_script("return document.querySelector('body > earth-app').shadowRoot.querySelector('#earth-relative-elements > earth-view-status').shadowRoot.querySelector('#pointer-coordinates')").text:
            #print("kd: ", u)
                        #n = d.execute_script("return document.querySelector('body > earth-app').shadowRoot.querySelector('#earth-relative-elements > earth-view-status').shadowRoot.querySelector('#pointer-coordinates')").text
                    action = webdriver.ActionChains(d)
                    #action.send_keys(Keys.ARROW_DOWN).perform()
                    action.key_down(Keys.ARROW_DOWN).perform()
                    time.sleep(0.4)
                    action.key_up(Keys.ARROW_DOWN).perform()
                        #action.key_down(Keys.ARROW_DOWN).perform()
                        #time.sleep(0.001)
                        #action.key_up(Keys.ARROW_DOWN).perform()
                    #print("kd")


                    #print([n[:9], n[12:21]])
                    #print(get_distance(float(n[:9]), float(n[12:21]), float(pp[u][:9]), float(pp[u][12:21])))
                    #d = drivers[u]
                    #nc = d.execute_script("return document.querySelector('body > earth-app').shadowRoot.querySelector('#earth-relative-elements > earth-view-status').shadowRoot.querySelector('#pointer-coordinates')").text
                    #dist = get_distance(float(pp[u][:9]), float(pp[u][12:21]), float(nc[:9]), float(nc[12:21]))
                    ##print(dist)
                    #while dist == 0 or dist > 6 or (float(pp[u][:9]) < float(nc[:9])):
                        #print(dist, float(pp[u][:9]) , float(nc[:9]))
                        #nc = d.execute_script("return document.querySelector('body > earth-app').shadowRoot.querySelector('#earth-relative-elements > earth-view-status').shadowRoot.querySelector('#pointer-coordinates')").text
                        #dist = get_distance(float(pp[u][:9]), float(pp[u][12:20]), float(nc[:9]), float(nc[12:20]))
                        #if dist == 0 or float(pp[u][:9]) < float(nc[:9]):
                            ##print("kd: ", u)
                        #    action = webdriver.ActionChains(d)
                        #    action.send_keys(Keys.ARROW_DOWN).perform()

                        #else:
                            ##print("ku: ", u)
                        #    action = webdriver.ActionChains(d)
                        #    action.send_keys(Keys.ARROW_UP).perform()
                        #nc = d.execute_script("return document.querySelector('body > earth-app').shadowRoot.querySelector('#earth-relative-elements > earth-view-status').shadowRoot.querySelector('#pointer-coordinates')").text
                        #dist = get_distance(float(pp[u][:9]), float(pp[u][12:21]), float(nc[:9]), float(nc[12:21]))


            for u in range(len(drivers)):
                d = drivers[u]

                if u in nd3:
                    continue

                if u in nd4:
                    continue

                cc = d.execute_script("return document.querySelector('body > earth-app').shadowRoot.querySelector('#earth-relative-elements > earth-view-status').shadowRoot.querySelector('#pointer-coordinates')").text
                #pp[u] = cc
                hh = d.execute_script("return document.querySelector('earth-app').shadowRoot.querySelector('earth-view-status').shadowRoot.querySelector('span#pointer-elevation')").text[:-1]
                ccl = [cc[:9], cc[12:21]]

                if hh == '' or hh == '0 c':
                    time.sleep(0.5)
                    hh = d.execute_script("return document.querySelector('earth-app').shadowRoot.querySelector('earth-view-status').shadowRoot.querySelector('span#pointer-elevation')").text[:-1]
                    if hh == '' or hh == '0 c':
                        continue

                if pp[u] != 0:
                    if get_distance(float(ccl[0]), float(ccl[1]), float(pp[u][0]), float(pp[u][1])) >15:
                        print("too big: ", get_distance(float(ccl[0]), float(ccl[1]), float(pp[u][0]), float(pp[u][1])))
                        if get_distance(float(ccl[0]), float(ccl[1]), float(pp[u][0]), float(pp[u][1])) >20:
                            action = webdriver.ActionChains(d)
                            #action.send_keys(Keys.ARROW_DOWN).perform()
                            action.key_down(Keys.ARROW_UP).perform()
                            time.sleep(0.7)
                            action.key_up(Keys.ARROW_UP).perform()
                        else:
                            action = webdriver.ActionChains(d)
                            #action.send_keys(Keys.ARROW_DOWN).perform()
                            action.key_down(Keys.ARROW_UP).perform()
                            time.sleep(0.5)
                            action.key_up(Keys.ARROW_UP).perform()

                pp[u] = ccl
                ##print("cc: ", cc, hh)
                if str(ccl[0]) + "," + str(ccl[1]) in dict[qq]:
                    print("error1", u, ccl)
                    continue
                #elif get_distance(float(pp[u][0]), float(pp[u][1]), float(ccl[0]), float(ccl[1])) > 10:
                #    print("error3", u)
                #    continue

                else:
                    if float(ccl[1]) not in [float(i[1]) for i in startpoints1[qq]]:
                        print("error2:", u, ccl)
                        continue
                    elif get_distance(coordinates[qq][0], coordinates[qq][1], float(ccl[0]), float(ccl[1])) > radius[qq]+10:

                        #print("done")
                        #print(cc, "nd3", u)
                        if len(startpoints2[qq]) != len(nd4):
                            #print(listofpoints[qq])
                            nd1.append(u)
                            nd2.append(u)
                            nd4.append(u)
                            pp[u] = 0
                        elif u not in nd3:
                            #print(listofpoints[qq])
                            nd3.append(u)
                            pp[u] = 0
                        continue
                    else:
                        #print("u", u, hh)
                        listofpoints[qq].append([float(ccl[0]), float(ccl[1])])
                        dict[qq][str(ccl[0]) + "," + str(ccl[1])] = [[float(ccl[0]), float(ccl[1])], hh]

        print("time2", time.time()  - start)
        print(qq)
        print(listofpoints[qq])
        print(dict[qq])
        print()
    for i in drivers:
        i.quit()
    return dict, listofpoints



                    #dict[i].append(int(float(driver.execute_script("return document.querySelector('earth-app').shadowRoot.querySelector('earth-view-status').shadowRoot.querySelector('span#pointer-elevation')").text[:-1])))
                #print("here")
            #for i in range(20):
            #    d = drivers[u]
            #    n = d.execute_script("return document.querySelector('body > earth-app').shadowRoot.querySelector('#earth-relative-elements > earth-view-status').shadowRoot.querySelector('#pointer-coordinates')").text
            #    print(n)
                #if float(n[:9]) < 50.11:
                #    print("-n")
                #    action.move_by_offset(0, -10).perform()
                #else:
                #    print("+n")
                #    action.move_by_offset(0, 10).perform()
                #if i == 0:
                #    action.move_by_offset(43, -100).click().perform()
                #elif i==1:
                #    action.move_by_offset(-43, 100).perform()
                #else:
            #    action.send_keys(Keys.ARROW_LEFT).perform()
                #    action.move_by_offset(0, 0.00001).perform()
                #print(driver.execute_script("return document.querySelector('body > earth-app').shadowRoot.querySelector('#earth-relative-elements > earth-view-status').shadowRoot.querySelector('#pointer-coordinates')").text)
            #    time.sleep(1)
            #    print()
            #print("done")
            #print(driver.execute_script("return document.querySelector('body > earth-app').shadowRoot.querySelector('#earth-relative-elements > earth-view-status').shadowRoot.querySelector('#pointer-coordinates')").text)
            #print()
        #driver.quit()
        #get_coordinates(50.110000, 8.680000,10, 0.00001, dict)


dict = []
listofpoints = []

coordinates = [[52.49740255, 13.36619249], [52.60454571, 13.36319707], [52.60014123, 13.36026063], [52.55904223, 13.4465941], [52.45530321, 13.47285728], [52.52526287, 13.52020803], [52.4230289, 13.49764475], [52.4314593, 13.57101704], [52.44001761, 13.57060789], [52.45583896, 13.55172236], [52.46883725, 13.55095641], [52.44414375, 13.43404008], [52.47607909, 13.46677445], [52.56115368, 13.40282171], [52.56349377, 13.40750518], [52.56807264, 13.41041617], [52.57030487, 13.40303118], [52.57367407, 13.41003417], [52.46455771, 13.40862411], [52.49097124, 13.41513372], [52.50005326, 13.41882849], [52.50601474, 13.41584766], [52.5153648, 13.4202064], [52.52977275, 13.41882503], [52.53278535, 13.41320706], [52.53889929, 13.41993493], [52.54158714, 13.41217307], [52.55036731, 13.41433531], [52.55347599, 13.42230274], [52.55646732, 13.41484948], [52.56301594, 13.42270297], [52.57060266, 13.41482461], [52.57524323, 13.41656167], [52.46423415, 13.41927803], [52.46737083, 13.42621207], [52.46918615, 13.42086517], [52.48320074, 13.4226264], [52.48522667, 13.42750659], [52.48852595, 13.42289628], [52.49043539, 13.42872343], [52.49316158, 13.42235992], [52.4974733, 13.4232651], [52.50274594, 13.42205561], [52.50482152, 13.430172], [52.50836631, 13.42309264], [52.52965031, 13.4326602], [52.53229719, 13.42529491], [52.54291463, 13.43379226], [52.54728576, 13.43503058], [52.55071609, 13.42788913], [52.55253336, 13.43497026], [52.55496923, 13.4284362], [52.55747096, 13.43549865], [52.55991157, 13.42931868], [52.46406384, 13.43294044], [52.46684558, 13.43972183], [52.47250757, 13.43426198], [52.47790055, 13.43368531], [52.48333384, 13.43491053], [52.48504533, 13.4414397], [52.48777312, 13.43385457], [52.48991148, 13.442432], [52.4926046, 13.43672936], [52.49822374, 13.43588085], [52.52396839, 13.44667039], [52.52889286, 13.44563447], [52.53308171, 13.44669275], [52.53572818, 13.44008015], [52.54081751, 13.43944363], [52.54532602, 13.4410948], [52.55468282, 13.44181992], [52.47400175, 13.45509465], [52.47739695, 13.44824294], [52.4788975, 13.45488673], [52.48207408, 13.44926456], [52.48451843, 13.45542621], [52.48973855, 13.45531505], [52.49275586, 13.45040366], [52.49478652, 13.46060261], [52.50399179, 13.45772313], [52.50509305, 13.44831397], [52.5133188, 13.45852131], [52.51818281, 13.45885242], [52.5208372, 13.45228777], [52.52289565, 13.4593748], [52.53011175, 13.45827514], [52.54544896, 13.45479748], [52.55004417, 13.45390582], [52.55445162, 13.45417585], [52.50035249, 13.46398074], [52.5038672, 13.47149106], [52.50550823, 13.46461993], [52.51003099, 13.46469576], [52.51552808, 13.46541626], [52.52001688, 13.46615253], [52.52991343, 13.46687813], [52.53394975, 13.46815903], [52.51063279, 13.47921792], [52.51791871, 13.4864989], [52.5201297, 13.47933022], [52.53569262, 13.48852059], [52.53850314, 13.48120374], [52.51178689, 13.49797518], [52.51703781, 13.49972187], [52.51937962, 13.49339331], [52.52078634, 13.49981064], [52.53196817, 13.49742986], [52.51951855, 13.50627869], [52.53231344, 13.36196627], [52.49245854, 13.35544521], [52.49145145, 13.36040064], [52.52649925, 13.50397372], [52.57507845, 13.38021312], [52.59290133, 13.37836726], [52.58467414, 13.3761146], [52.4827607, 13.4078243], [52.54601483, 13.42227515], [52.54439388, 13.42772631], [52.43839273, 13.47178707], [52.41950342, 13.43436993], [52.53289408, 13.37984643], [52.53171982, 13.43702025], [52.53467961, 13.41943888], [52.52994397, 13.41072818], [52.50989492, 13.37973039], [52.50847168, 13.37549874], [52.50522883, 13.36833412], [52.50647705, 13.40197193], [52.52577699, 13.40396217], [52.49015245, 13.44876211], [52.48195605, 13.46918621], [52.36707414, 13.51421038], [52.36158448, 13.50960569], [52.37070758, 13.52438266], [52.37472829, 13.54179239], [52.38601614, 13.53272058], [52.47329071, 13.42550218], [52.47972735, 13.44356531], [52.49947293, 13.3633783], [52.45782489, 13.37631722], [52.56894138, 13.37687427], [52.57230512, 13.36308282], [52.57222281, 13.37274309], [52.5421152, 13.35736135], [52.5328447, 13.37238942], [52.3675059, 13.42492377], [52.38009586, 13.44529639], [52.36464481, 13.44150163], [52.38863288, 13.49908214], [52.37104388, 13.4784734], [52.34667645, 13.44511977], [52.39612784, 13.44232937], [52.40681986, 13.44114096], [52.40590629, 13.46725465], [52.39014249, 13.51961036], [52.35642743, 13.47556826], [52.36714252, 13.55497186], [52.38276438, 13.55553717], [52.52333739, 13.40392896], [52.53199851, 13.40644239], [52.52942403, 13.40436114], [52.52872646, 13.39816983], [52.53684828, 13.37860808], [52.55598926, 13.38781365], [52.4761047, 13.44045225], [52.47211404, 13.44253822], [52.52276106, 13.40964714], [52.35521034, 13.43253187], [52.51502641, 13.39994068], [52.50899926, 13.40421435], [52.47339532, 13.44932346], [52.47504288, 13.36800479], [52.46934274, 13.38603707], [52.4995599, 13.37737206], [52.49933036, 13.39676904], [52.49888835, 13.4072709], [52.50067355, 13.42732384], [52.50097159, 13.43222977], [52.49956158, 13.45854282], [52.50649964, 13.47022444], [52.50679542, 13.47693358], [52.50928328, 13.49003472], [52.50341213, 13.48582486], [52.47685276, 13.42123539], [52.49597012, 13.35970767], [52.47989964, 13.42497726], [52.52679891, 13.37192272], [52.5251753, 13.39129293], [52.52040978, 13.38979927], [52.5122124, 13.38908517], [52.51169863, 13.4170605], [52.51254318, 13.43723947], [52.52331426, 13.43708073], [52.52518754, 13.41870536], [52.5327167, 13.42958117], [52.53511537, 13.43451221], [52.54692442, 13.41487158], [52.54703136, 13.38988776], [52.5517978, 13.36009906], [52.56528201, 13.39714804], [52.5653632, 13.41818753], [52.55710104, 13.39248921], [52.6299371, 13.46346451], [52.54652887, 13.39847094], [52.54842309, 13.40725378], [52.55276738, 13.40200538], [52.55385663, 13.40647109], [52.5433028, 13.363106], [52.54685502, 13.36663682], [52.54965949, 13.42124933], [52.50445793, 13.38272626], [52.50886635, 13.37226103], [52.49054705, 13.40952109], [52.4814062, 13.43145342], [52.52248791, 13.39840719], [52.51764711, 13.40598719], [52.5078097, 13.38418265], [52.50796341, 13.39201193], [52.50757881, 13.40752834], [52.50941084, 13.44662838], [52.51096369, 13.45137963], [52.50827328, 13.45943682], [52.50190428, 13.47755427], [52.51714997, 13.37765325], [52.51340711, 13.39359103], [52.49267745, 13.37627881], [52.49404054, 13.38341207], [52.48567035, 13.38021733], [52.4828996, 13.37364752], [52.597687, 13.462925], [52.53280182, 13.38654826], [52.53635606, 13.39456542], [52.51950259, 13.41382523], [52.52187088, 13.415107], [52.52431867, 13.41316245], [52.52606357, 13.4108837], [52.55982227, 13.38151441], [52.47602197, 13.47800404], [52.43124988, 13.43559491], [52.56006423, 13.41364377], [52.55473807, 13.39371538], [52.51592115, 13.42757208], [52.53288367, 13.48250672], [52.52672904, 13.49114875], [52.52664257, 13.47131322], [52.55854626, 13.37660243], [52.57127141, 13.42484051], [52.48310847, 13.38559263], [52.48151762, 13.38985987], [52.52072345, 13.42990817], [52.57229069, 13.54967033], [52.50832693, 13.43609449], [52.50488284, 13.44102009], [52.5173659, 13.47136619], [52.51474253, 13.48095504], [52.51371909, 13.49028797], [52.51030703, 13.47113771], [52.51696047, 13.45307201], [52.51903135, 13.44680626], [52.5172613, 13.43671772], [52.49735248, 13.38954581], [52.50490352, 13.39058728], [52.50644876, 13.37586721], [52.50738654, 13.36293886], [52.4615565, 13.38147758], [52.48983971, 13.38993994], [52.54118985, 13.42494818], [52.55066275, 13.39248388], [52.5328268, 13.39917326], [52.53663612, 13.4102236], [52.54943527, 13.44554457], [52.54820149, 13.46384142], [52.52349888, 13.48482582], [52.53619374, 13.45423353], [52.54303873, 13.44826742], [52.50192034, 13.45115376], [52.48532188, 13.36376572], [52.52389282, 13.36674551], [52.50823418, 13.39695406], [52.51581889, 13.41087983], [52.51213865, 13.40882858], [52.48762176, 13.44863656], [52.52057791, 13.39469408], [52.52108819, 13.4216968], [52.51343487, 13.4749671], [52.51284653, 13.46727443], [52.56284112, 13.37356593], [52.52423835, 13.37901882], [52.47766809, 13.37409365], [52.45955355, 13.40121549], [52.52731679, 13.45465734], [52.52420257, 13.45254192], [52.52717314, 13.42537297], [52.52387169, 13.426681], [52.5438024, 13.415645080000001], [52.56690542, 13.40208944], [52.55852353, 13.42243409], [52.54259891, 13.39228078], [52.54029099, 13.36719942], [52.49513795, 13.40633499], [52.49565105, 13.41504919], [52.50294967, 13.40704524], [52.50263477, 13.41482413], [52.49863499, 13.42761823], [52.50985095, 13.45586309], [52.52326669, 13.47307619], [52.5290467, 13.48067707], [52.5117959, 13.40147343], [52.51383832, 13.3865201], [52.51583727, 13.38928593], [52.51827155, 13.39027781], [52.52558525, 13.39866937], [52.53422871, 13.40497937], [52.53618312, 13.42776086], [52.54333243, 13.41956318], [52.54366007, 13.47309923], [52.55324027, 13.44845557], [52.52860999, 13.3640226], [52.53972852, 13.4461459], [52.51381747, 13.44599117], [52.51435726, 13.47072587], [52.5305174, 13.38339955], [52.52961704, 13.37887273], [52.46978445, 13.45107033], [52.56719435, 13.36702436], [52.56705074, 13.42708863], [52.5534337, 13.41395693], [52.55149305, 13.41839643], [52.54908686, 13.40247694], [52.48022218, 13.43667573], [52.4686572, 13.43093532], [52.46961664, 13.43533911], [52.48194509, 13.44015873], [52.50037398, 13.44045689], [52.49625207, 13.44213403], [52.4974244, 13.44798608], [52.51167369, 13.37591996], [52.51035573, 13.38762502], [52.5107958, 13.43012311], [52.55279217, 13.38689822], [52.4954664, 13.42990538], [52.42674595, 13.40227922], [52.38422666, 13.41926681], [52.39967336, 13.41010224], [52.39698537, 13.38343987], [52.38889971, 13.39154716], [52.62758047, 13.42993163], [52.40378887, 13.35821508], [52.41515528, 13.35999837], [52.42367562, 13.35758905], [52.43259877, 13.36055464], [52.44095438, 13.36254955], [52.44957794, 13.36340317], [52.45805154, 13.3644191], [52.46678913, 13.36510815], [52.58752374, 13.35639301], [52.59200113, 13.3653115], [52.60447984, 13.3786925], [52.63017909, 13.38149891], [52.40540069, 13.38439231], [52.41904626, 13.37252857], [52.42282175, 13.38522618], [52.42761269, 13.37346612], [52.4332374, 13.39234735], [52.43621821, 13.37431968], [52.44031234, 13.38667142], [52.44428169, 13.37552007], [52.44662809, 13.39472908], [52.45322111, 13.37630196], [52.5759253, 13.40051531], [52.58253808, 13.39181659], [52.58592323, 13.40223279], [52.59111384, 13.38975781], [52.5996293, 13.39061063], [52.61883839, 13.39397202], [52.38102815, 13.40198526], [52.38870508, 13.40562693], [52.39449526, 13.39853785], [52.40097934, 13.39531464], [52.40698292, 13.41264072], [52.40951841, 13.39601791], [52.4176198, 13.3950127], [52.43895727, 13.40881647], [52.44785413, 13.41220084], [52.45320693, 13.3973273], [52.45629674, 13.41307575], [52.57876386, 13.42702271], [52.58198022, 13.41087341], [52.58551566, 13.4264825], [52.59044587, 13.41093864], [52.59389243, 13.43251578], [52.59879377, 13.41497746], [52.60690099, 13.41997979], [52.6152756, 13.41927283], [52.39233664, 13.42023065], [52.41796154, 13.41350706], [52.42676406, 13.4166265], [52.43644615, 13.42791641], [52.43924922, 13.44380079], [52.44304359, 13.42390126], [52.45161046, 13.42482021], [52.45392604, 13.4395361], [52.55901874, 13.45623706], [52.56471719, 13.4392367], [52.56900324, 13.45344191], [52.57214975, 13.43693827], [52.58058968, 13.43788068], [52.58618422, 13.44443868], [52.59310915, 13.45140138], [52.60173478, 13.45218883], [52.60642895, 13.44029042], [52.64089059, 13.4440525], [52.42630558, 13.452631], [52.42902779, 13.45981647], [52.43860504, 13.45858286], [52.44602061, 13.46098441], [52.45067452, 13.44924184], [52.45923421, 13.44987068], [52.46367639, 13.46227576], [52.5577897, 13.4722763], [52.56639166, 13.47321205], [52.57579449, 13.46272776], [52.59195113, 13.46984479], [52.60080817, 13.4767242], [52.60760384, 13.46352314], [52.61084702, 13.49259658], [52.61538312, 13.47184452], [52.40606677, 13.48850824], [52.41235445, 13.48215678], [52.42052586, 13.48015883], [52.43033172, 13.47505133], [52.4335776, 13.48687054], [52.44688068, 13.48336234], [52.46230235, 13.47504061], [52.46566335, 13.48868474], [52.47187925, 13.46880077], [52.49566172, 13.47068057], [52.49689259, 13.49086021], [52.53965272, 13.49499505], [52.54579919, 13.48945285], [52.55288313, 13.4839892], [52.55879362, 13.49640049], [52.56769681, 13.50191523], [52.57743322, 13.48389795], [52.58508157, 13.49406], [52.62174071, 13.49130286], [52.6256228, 13.50372727], [52.63028297, 13.49238623], [52.64170864, 13.5131881], [52.40359361, 13.5065501], [52.41253759, 13.49987219], [52.4268695, 13.5079936], [52.44027201, 13.49724149], [52.44409531, 13.50975536], [52.4525044, 13.50932468], [52.46831007, 13.51136769], [52.47850857, 13.51333926], [52.47983289, 13.50035295], [52.48707878, 13.51415929], [52.49604689, 13.51376349], [52.49961751, 13.49964064], [52.50444855, 13.51939136], [52.50853274, 13.5042301], [52.51305142, 13.51682577], [52.53052493, 13.51727265], [52.53871913, 13.51946497], [52.54331648, 13.50793445], [52.54798316, 13.50714643], [52.55452016, 13.51560797], [52.56053021, 13.51031533], [52.56434524, 13.52177907], [52.56876729, 13.51299756], [52.40312576, 13.5253525], [52.41351429, 13.51889143], [52.41353232, 13.5366857], [52.43068943, 13.52103414], [52.43641117, 13.5284261], [52.44034472, 13.54033337], [52.45112526, 13.52236487], [52.46182049, 13.52051564], [52.47765706, 13.53790129], [52.48205875, 13.52589657], [52.4844335, 13.53903168], [52.49080581, 13.52679631], [52.49480029, 13.53946315], [52.51310096, 13.53001507], [52.52235195, 13.53072868], [52.52819383, 13.54010722], [52.53826499, 13.54287379], [52.55266818, 13.55980027], [52.57708114, 13.53368434], [52.39756133, 13.53789717], [52.40409133, 13.54262302], [52.41270137, 13.55678422], [52.42038138, 13.53819494], [52.4251951, 13.5572096], [52.430792, 13.54044014], [52.4334065, 13.55706998], [52.44213203, 13.55851897], [52.47661691, 13.56208937], [52.48982877, 13.55852013], [52.49859847, 13.55205309], [52.50242656, 13.56476635], [52.50719953, 13.55300246], [52.51736492, 13.54945367], [52.51970456, 13.5665607], [52.52439499, 13.55460691], [52.52823485, 13.56747677], [52.54145356, 13.55649397], [52.5457514, 13.56915112], [52.55409899, 13.57013809], [52.55958219, 13.55772357], [52.56742329, 13.55922011], [52.56666366, 13.57233709], [52.39348456, 13.57254543], [52.40234544, 13.56138553], [52.41032915, 13.57356257], [52.45350951, 13.56834345], [52.47180738, 13.57384052], [52.48501637, 13.57066802], [52.47846776, 13.36058842], [52.48340311, 13.35972156], [52.5836697, 13.46851208], [52.57613792, 13.51188632], [52.58860235, 13.53535511], [52.56622223, 13.53129255], [52.48662473, 13.36018689], [52.45922061, 13.4325435], [52.44656476, 13.57022137], [52.45689709, 13.53327104], [52.46091219, 13.50534497], [52.448007, 13.38389692], [52.60172504, 13.43101782], [52.48936435, 13.49683618], [52.46886999, 13.47962725], [52.63330371, 13.50754879], [52.45656212, 13.38644995], [52.54622372, 13.54690313], [52.55480685, 13.5428271], [52.64318731, 13.49548722], [52.50255897, 13.36163476], [52.5193111, 13.35615358], [52.52472633, 13.35739833], [52.53430226, 13.35926274], [52.53559407, 13.36557773], [52.53949943, 13.35812587], [52.54761058, 13.35872419], [52.55100537, 13.36705083], [52.55531244, 13.36687407], [52.55803717, 13.35996609], [52.56056259, 13.36844454], [52.56265036, 13.35953855], [52.56752495, 13.36129261], [52.57769504, 13.36265814], [52.46302646, 13.37111822], [52.48140797, 13.36611574], [52.48766833, 13.37381592], [52.48988421, 13.36851903], [52.49434532, 13.36734051], [52.50125122, 13.36859091], [52.50139631, 13.37434051], [52.52163089, 13.37700298], [52.5373272, 13.37211409], [52.54332252, 13.37129423], [52.54506392, 13.3785707], [52.54774918, 13.37445042], [52.54978776, 13.38001585], [52.55295125, 13.37464399], [52.55533322, 13.37968345], [52.56454257, 13.38075011], [52.46635506, 13.37877468], [52.47536795, 13.37931739], [52.4802226, 13.37990349], [52.48733336, 13.38745442], [52.48988383, 13.38067343], [52.49237127, 13.3881926], [52.49948987, 13.38171845], [52.50155053, 13.38885767], [52.51374885, 13.38175316], [52.51858805, 13.38372512], [52.52299804, 13.38562523], [52.52784746, 13.38610919], [52.53032421, 13.39173115], [52.53822114, 13.38634814], [52.53956721, 13.39358485], [52.56174866, 13.38803477], [52.56711452, 13.38793644], [52.45998795, 13.39105389], [52.46532316, 13.39105548], [52.48450113, 13.39405914], [52.48853614, 13.39466837], [52.49145285, 13.40150884], [52.49410404, 13.39494444], [52.49628378, 13.40079811], [52.50325765, 13.39581482], [52.51868661, 13.39743953], [52.53746185, 13.40047624], [52.53982046, 13.4070771], [52.54277783, 13.39906094], [52.55643457, 13.40125603]]

antennah = [36, 43, 52, 25, 25, 35, 36, 25, 30, 25, 25, 25, 33, 30, 28, 35, 32, 32, 30, 27, 41, 37, 37, 34, 34, 29, 25, 33, 29, 35, 30, 35, 25, 25, 28, 30, 27, 30, 34, 29, 33, 32, 32, 27, 35, 32, 32, 32, 26, 29, 27, 29, 25, 25, 31, 29, 26, 33, 32, 29, 35, 25, 37, 31, 31, 30, 25, 25, 28, 29, 25, 30, 31, 31, 29, 25, 33, 36, 35, 30, 33, 25, 25, 28, 25, 33, 27, 30, 28, 28, 36, 33, 32, 29, 29, 37, 28, 41, 35, 28, 32, 28, 28, 28, 25, 30, 25, 26, 33, 30, 33, 25, 30, 30, 30, 25, 30, 30, 30, 36, 30, 30, 30, 30, 38, 30, 35, 30, 30, 30, 25, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 32, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 29, 28, 35, 33, 27, 28, 29, 29, 29, 27, 27, 27, 30, 32, 30, 32, 34, 37, 38, 28, 41, 34, 38, 30, 30, 33, 28, 29, 27, 27, 30, 40, 28, 32, 28, 30, 29, 31, 28, 32, 43, 30, 28, 29, 31, 37, 37, 27, 30, 30, 29, 29, 27, 32, 27, 32, 27, 30, 30, 33, 28, 32, 33, 45, 27, 30, 30, 25, 25, 28, 32, 41, 29, 42, 28, 25, 33, 40, 38, 25, 40, 30, 30, 28, 27, 28, 30, 26, 32, 29, 31, 34, 32, 27, 29, 30, 33, 31, 28, 25, 25, 27, 30, 35, 27, 29, 33, 33, 35, 34, 30, 27, 33, 28, 29, 25, 30, 25, 25, 30, 30, 30, 36, 30, 25, 25, 30, 30, 30, 30, 30, 30, 32, 30, 25, 33, 38, 30, 35, 30, 30, 30, 30, 30, 25, 25, 25, 25, 30, 30, 30, 30, 25, 25, 25, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 39, 30, 30, 30, 30, 25, 30, 30, 33, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 35, 30, 30, 30, 32, 30, 30, 30, 36, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 33, 35, 30, 30, 30, 33, 30, 30, 33, 30, 37, 30, 30, 30, 30, 30, 30, 30, 40, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 36, 35, 35, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 33, 34, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 37, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 31, 30, 30, 30, 30, 35, 32, 30, 35, 30, 30, 30, 30, 35, 30, 30, 30, 30, 35, 30, 30, 30, 35, 30, 31, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 39, 30, 30, 27, 30, 35, 35, 30, 30, 30, 30, 30, 30, 30, 30, 28, 30, 30, 30, 30, 35, 30, 30, 35, 30, 30, 32, 30, 30, 31, 25, 40, 30, 30, 30, 33, 30, 30, 35, 30, 30, 30, 30, 30, 30, 30, 28, 28, 28, 29, 35, 32, 35, 28, 31, 31, 32, 26, 25, 27, 29, 25, 25, 25, 25, 31, 27, 33, 30, 31, 36, 33, 33, 33, 30, 35, 30, 31, 27, 33, 25, 25, 25, 25, 32, 33, 32, 33, 26, 36, 37, 27, 33, 34, 26, 25, 25, 31, 30, 32, 30, 29, 34, 37, 25, 31, 32, 30, 25]
radius = [150, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 200, 200, 200, 200, 150, 150, 150, 150, 150, 100, 150, 150, 150, 150, 150, 150, 200, 200, 200, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 200, 200, 200, 200, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 200, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 200, 200, 200, 200, 200, 150, 150, 150, 150, 150, 150, 200, 200, 150, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 150, 150, 150, 200, 300, 300, 300, 150, 150, 150, 300, 300, 150, 150, 150, 150, 100, 100, 100, 100, 150, 150, 300, 300, 300, 300, 300, 300, 150, 150, 150, 200, 200, 200, 200, 150, 150, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 100, 150, 150, 150, 150, 150, 150, 150, 100, 300, 100, 100, 150, 150, 200, 100, 150, 150, 150, 150, 150, 150, 150, 200, 150, 150, 150, 150, 150, 150, 100, 100, 150, 150, 150, 100, 150, 150, 150, 150, 150, 200, 200, 150, 300, 150, 150, 150, 150, 150, 150, 150, 100, 100, 150, 150, 100, 100, 100, 100, 150, 150, 150, 150, 150, 100, 100, 150, 150, 150, 150, 300, 150, 150, 100, 100, 100, 100, 150, 300, 300, 200, 150, 150, 200, 200, 200, 200, 200, 150, 150, 150, 300, 150, 150, 150, 200, 200, 150, 150, 150, 150, 150, 100, 100, 100, 200, 150, 150, 150, 150, 150, 200, 200, 200, 200, 200, 150, 150, 150, 100, 100, 100, 150, 100, 150, 150, 150, 200, 150, 150, 300, 200, 150, 150, 150, 150, 200, 200, 150, 150, 150, 150, 150, 150, 150, 150, 200, 200, 100, 100, 100, 100, 150, 150, 150, 150, 200, 200, 150, 200, 150, 150, 150, 150, 150, 200, 200, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 100, 100, 150, 150, 150, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 200, 200, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 150, 150, 300, 300, 300, 300, 150, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 100, 150, 150, 150, 150, 150, 150, 150, 200, 200, 200, 200, 200, 150, 200, 150, 150, 150, 150, 150, 100, 150, 150, 150, 150, 150, 150, 150, 150, 200, 200, 150, 150, 150, 150, 150, 100, 100, 100, 100, 150, 150, 150, 150, 150, 200, 200, 200, 200, 150, 150, 150, 150, 150, 100, 100, 150, 150, 150, 150]
print(radius[31])
dict, listofpoints = bf(coordinates[40:], radius[40:])

print(dict)
print(listofpoints)
#a = []
#b = []
#get_starting_points(52.49740255, 13.36619249, 150, a, b)

#print(len(a))
