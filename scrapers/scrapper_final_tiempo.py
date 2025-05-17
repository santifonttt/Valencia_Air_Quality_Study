import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime

def iniciar_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--start-maximized')
    driver = webdriver.Chrome(options=options)
    return driver

def aceptar_cookies(driver):
    try:
        boton_aceptar = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[14]/div[2]/div[2]/div[2]/div[2]/button[1]'))
        )
        boton_aceptar.click()
        print("Cookies aceptadas.")
    except Exception as e:
        print("No apareció el popup de cookies o ya fue aceptado.")

def seleccionar_año(driver, year):
    try:
        boton = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, f'button.gray-button[data-year="{year}"]'))
        )
        driver.execute_script("arguments[0].scrollIntoView();", boton)
        boton.click()
        print(f"Año {year} seleccionado.")
        time.sleep(0.25)  
    except Exception as e:
        print(f"No se pudo seleccionar el año {year}: {e}")

def extraer_datos(driver, dia, mes, year, resultados):
    driver.get(f"https://www.tiempo3.com/europe/spain/comunidad-valenciana/valencia?page=past-weather#day={dia}&month={mes}")
    driver.execute_script("document.body.style.zoom='0.1'")  

    seleccionar_año(driver, year)

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".day_table"))
        )
        filas = driver.find_elements(By.CSS_SELECTOR, ".day_table tbody tr")

        datos = {"Día": dia, "Mes": mes, "Año": year}

        for fila in filas:
            nombre_fila = fila.find_element(By.TAG_NAME, "th").text
            celdas = fila.find_elements(By.TAG_NAME, "td")
            datos[nombre_fila] = [celda.text for celda in celdas]

        resultados.append(datos)

    except Exception as e:
        print(f"No se pudieron extraer datos para {dia}/{mes}/{year}: {e}")

def guardar_csv(resultados):
    df = pd.DataFrame(resultados)
    df.to_csv("historico_valencia.csv", index=False, mode='a', header=not pd.io.common.file_exists("historico_valencia.csv"))
    print("Datos guardados en 'historico_valencia.csv'")

def main():
    driver = iniciar_driver()
    driver.get("https://www.tiempo3.com/europe/spain/comunidad-valenciana/valencia?page=past-weather")
    aceptar_cookies(driver)

    años = range(2020, 2026)
    meses = range(1, 13)
    dias = range(1, 32)

    hoy = datetime.now()

    resultados = []

    for mes in meses:
        for dia in dias:
            resultados = []
            for year in años:
                
                if mes == 2 and dia > 28:
                    continue
                if mes in [4, 6, 9, 11] and dia > 30:
                    continue

                fecha_actual = datetime(year, mes, dia)

                if fecha_actual > hoy:
                    print(f"Saltando fecha futura: {dia}/{mes}/{year}")
                    continue
                
                extraer_datos(driver, dia, mes, year, resultados)

            if resultados:
                guardar_csv(resultados)

    driver.quit()

if __name__ == "__main__":
    main()

