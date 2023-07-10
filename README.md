## **TASK 1: Konfiguracja oprogramowania** :white_check_mark:
* ### _**SUBTASK 1: Dlaczego zdecydowałem się wziąć udział w wyzwaniu Dare IT Challenge?**_
**Cześć!** 😃 Mam na imię Magda. Zdecydowałam się na udział w programie, aby poszerzyć swoją wiedzę z obszaru testowania automatycznego. Ukończyłam już jeden kurs stworzony przez Dare IT z testowania manualnego, ale moim głównym celem jest, aby zdobyć doświadczenie w testowaniu automatycznym i stworzyć nowy projekt do swojego portfolio.

Będąc absolwentem już jednego kursu stworzonego przez Patrycję, jestem pewna, że zakończę go z dużą dawką nowej dla mnie wiedzy i będę bardzo z niego zadowolona :smile:

* ### _**SUBTASK 4: Test ISTQB "Purpurowy"**_
Zdobyłam 10/14 punktów :sparkles:

![Przechwytywanie](https://github.com/szatmagda/Challenge_Portfolio_Magda02/assets/116760612/de43e670-270d-4bf0-b450-01fd7e071b64)


## **TASK 2: Selektory** :white_check_mark:
* ### _**SUBTASK 2: Wyszukiwanie selektorów na stronie logowania**_

:crystal_ball: **1. remind_password_hyperlink_xpath**
```
//*[@id="__next"]/form/div/div[1]/a
//a[@tabindex='-1']
//*[text()='Remind password']
```
:crystal_ball: **2. sign_in_button_xpath**
```
//button[@tabindex='0']
//*[@id="__next"]/form/div/div[2]/button
//button[@type='submit']
```
:crystal_ball: **3. language_en_button_xpath**
```
//*[@id="__next"]/form/div/div[2]/div/div
//div[@tabindex='0']
//*[text()='English']
```
:crystal_ball: **4. language_pl_button_xpath**
```
//*[@id="__next"]/form/div/div[2]/div/div
//div[@tabindex='0']
//div[text()='Polski']
```
:crystal_ball: **5. login_field_xpath**
```
//*[@id="login"]
//*[@name='login']
//*[@type='text']
```
:crystal_ball: **6. password_field_xpath**
```
//*[@id="password"]
//*[@name='password']
//*[@type='password']
```
* ### _**SUBTASK 3: Dodawanie selektorów do projektu**_
[login_page.py](https://github.com/szatmagda/Challenge_Portfolio_Magda02/blob/main/pages/login_page.py)

* ### _**SUBTASK 4: Dodanie nowego pliku: dashboard.py**_
[dashboard.py](https://github.com/szatmagda/Challenge_Portfolio_Magda02/blob/main/pages/dashboard.py)

* ### _**SUBTASK 5: Dodanie nowego pliku: add_a_match_form.py**_
[add_a_match_form.py](https://github.com/szatmagda/Challenge_Portfolio_Magda02/blob/main/pages/add_a_match_form.py)
