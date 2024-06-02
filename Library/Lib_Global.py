from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import sys
sys.path.append("D:/Automation Testing/Selenium-Python---First-Project/Library")
from Lib_Excel import LibExcel
# File Excel
filePath = "D:/Automation Testing/Selenium-Python---First-Project/File Excel/Travelio_Login.xlsx"
sheetName = "Travelio_Login"

# Inisialisasi WebDriver
driver = webdriver.Chrome()
driver.maximize_window()

# Buka halaman web
def OpenWebPage():
    driver.get("https://www.travelio.com/")
    time.sleep(5)

#Login
def Login():
    #Objek yang ada di Home Page Travelio
    modalIklan   = driver.find_element(By.XPATH, '//div[@id="tpmModal"]')
    modalClose   = driver.find_element(By.XPATH, '//i[@class="fa fa-close fa-lg close padding15"]')
    menuTravelio = driver.find_element(By.XPATH, '//*[@id="menu-wrapper"]')
    btnLogin     = driver.find_element(By.XPATH, '//*[@id="loginBtn"]')

    #Objek yang ada di Modal Login Page
    tabMasuk      = driver.find_element(By.XPATH, '//*[@id="login-modal-sign-in-tab"]')
    inputUsername = driver.find_element(By.XPATH, '//input[@id="login-email"]')
    inputPassword = driver.find_element(By.XPATH, '//input[@id="login-password"]')
    btnMasuk      = driver.find_element(By.XPATH, '//button[@id="login-modal-btn"]')

    # username    = 'yusuftriwibowo000@gmail.com'
    username    = LibExcel.getDataExcel(filePath, "USERNAME", sheetName)
    password    = LibExcel.getDataExcel(filePath, "PASSWORD", sheetName)
    greet       = LibExcel.getDataExcel(filePath, "NAME", sheetName)
    #Jika muncul popup iklan
    if modalIklan:
        modalClose.click()
    else:
        print('Popup Iklan tidak ada di page')

    if menuTravelio and btnLogin:
        #'Btn Login' di home page
        driver.execute_script("arguments[0].click();", btnLogin)
        time.sleep(5)
        if tabMasuk:
            tabMasuk.click()
            if inputUsername and inputPassword:
                inputUsername.send_keys(username)
                time.sleep(1)
                inputPassword.send_keys(password)
                time.sleep(1)
                if btnMasuk:
                    btnMasuk.click()
                    time.sleep(5)
                    #Jika Berhasil Login
                    dropdownUser = None
                    try:
                        dropdownUser = driver.find_element(By.XPATH, '//div[@id="user-dropdown"]/div[@id="user-option"]/span[text()="' + greet +'"]')
                    except Exception as e:
                        pass
                    
                    try:
                        usernamePasswordSalah   = driver.find_element(By.XPATH, '//div[@id="modal-error-message" and text()="Email atau password salah"]')
                        btnModalOK              = driver.find_element(By.XPATH, '//button[@class="col-xs-12 btn btn-tosca"]')
                    except Exception as e:
                        pass

                    if dropdownUser:
                        print("Berhasil Login")
                        Logout()
                    elif usernamePasswordSalah :
                        btnModalOK.click()
                        print("Username atau Password Salah")
                        driver.quit()
                    else:
                        print("Gagal Login")
                        driver.quit()
                else:
                    print('Button Submit Login tidak ada di page')
                    driver.quit()
            else:
                print('Field Username dan Password tidak ada di page')
                driver.quit()
        else:
            print('Tab Masuk tidak tampil di page')      
            driver.quit()          
    else:
        print('Gagal Masuk Travelio Page')
        driver.quit()

#Logout
def Logout():

    # dropdown = None

    # try:
    dropdown = driver.find_element(By.ID, 'user-dropdown')
    # except:
    #     pass

    try:
        dropdown.click()
        time.sleep(2)
        btnLogout = driver.find_element(By.XPATH, '//a[@onclick="userLogout()"]')
        if btnLogout:
            btnLogout.click()
            time.sleep(5)
            btnLogin = driver.find_element(By.XPATH, '//*[@id="loginBtn"]')
            if btnLogin:
                print("Berhasil Logout")
                # Tutup browser
                driver.quit()
            else:
                print("Gagal Logout")
        else:
            print("Button Logout tidak ada")

    except Exception as e:
        print('Dropdown user tidak tampil di page')