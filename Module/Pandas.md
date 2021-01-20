# Pandas
> Pandas Library<br>
> 데이터 분석 라이브러리<br>

## **Pandas Library**
- pandas : python의 data analysis의 핵심 library
- pandas는 고유하게 정의된 두개의 자료구조를 이용(시리즈, 데이터프레임)
- pandas Series : numpy의 1차원 배열과 유사하다.
- 시리즈 안에 값들이 같은 데이터 타입을 가진다.  ※ numpy는 모든 타입을 넣을 수 있지만 series는 불가능
- pandas DataFrame : numpy의 2차원 배열과 유사하다.   ※ 3차원 배열과 유사한건 없음.
- Series를 여러개 컬럼형태로 모아 놓은게 DataFrame이라고 한다.
- 다른 데이터 타입을 가져도 된다.


* 터미널 실행


        $ KANGs-MacBook-Pro ~ $ cd ~
          ↳ cd ~ : 최상위 폴더로 이동

* 가상환경 접속


        $ KANGs-MacBook-Pro ~ $ source activate data_env

* Pandas 설치


        $ (data_env) KANGs-MacBook-Pro:~ kang$ conda install pandas
        Solving environment: done
        
        
        ==> WARNING: A newer version of conda exists. <==
          current version: 4.5.12
          latest version: 4.6.4
        
        Please update conda by running
        
            $ conda update -n base -c defaults conda
        
        
        
        ## Package Plan ##
        
          environment location: /anaconda3/envs/data_env
        
          added / updated specs: 
            - pandas
        
        
        The following packages will be downloaded:
        
            package                    |            build
            ---------------------------|-----------------
            pytz-2018.9                |           py36_0         261 KB
            pandas-0.24.1              |   py36h0a44026_0        10.1 MB
            ------------------------------------------------------------
                                                   Total:        10.3 MB
        
        The following NEW packages will be INSTALLED:
        
            pandas: 0.24.1-py36h0a44026_0
            pytz:   2018.9-py36_0        
        
        
        Proceed ([y]/n)? y
         ↳ 설치를 원할 시 y 버튼을 클릭하고 엔터!

        
        Downloading and Extracting Packages
        pytz-2018.9          | 261 KB    | ##################################### | 100% 
        pandas-0.24.1        | 10.1 MB   | ##################################### | 100% 
        Preparing transaction: done
        Verifying transaction: done
        Executing transaction: done


 
* 이제 jupyter notebook에서 판다스 import 사용 가능.

