# PyMySQL
> MySQL을 사용하기 위해 module<br>

## **PyMySQL 설치**

* 터미널 실행


        $ KANGs-MacBook-Pro ~ $ cd ~
          ↳ cd ~ : 최상위 폴더로 이동

* 가상환경 접속


        $ KANGs-MacBook-Pro ~ $ source activate data_env

* pymysql 설치


        $ (data_env) KANGs-MacBook-Pro:~ kang$ conda install pymysql
        Solving environment: done
        
        
        ==> WARNING: A newer version of conda exists. <==
          current version: 4.5.12
          latest version: 4.6.4
        
        Please update conda by running
        
            $ conda update -n base -c defaults conda
        
        
        
        ## Package Plan ##
        
          environment location: /anaconda3/envs/data_env
        
          added / updated specs: 
            - pymysql
        
        
        The following packages will be downloaded:
        
            package                    |            build
            ---------------------------|-----------------
            idna-2.8                   |           py36_0         133 KB
            pymysql-0.9.3              |           py36_0          83 KB
            asn1crypto-0.24.0          |           py36_0         154 KB
            cffi-1.11.5                |   py36h6174b99_1         205 KB
            cryptography-2.5           |   py36ha12b0ac_0         590 KB
            pycparser-2.19             |           py36_0         173 KB
            ------------------------------------------------------------
                                                   Total:         1.3 MB
        
        The following NEW packages will be INSTALLED:
        
            asn1crypto:   0.24.0-py36_0        
            cffi:         1.11.5-py36h6174b99_1
            cryptography: 2.5-py36ha12b0ac_0   
            idna:         2.8-py36_0           
            pycparser:    2.19-py36_0          
            pymysql:      0.9.3-py36_0         
        
        
        Proceed ([y]/n)? y
         ↳ 설치를 원할 시 y 버튼을 클릭하고 엔터!
        
        
        Downloading and Extracting Packages
        idna-2.8             | 133 KB    | ##################################### | 100% 
        pymysql-0.9.3        | 83 KB     | ##################################### | 100% 
        asn1crypto-0.24.0    | 154 KB    | ##################################### | 100% 
        cffi-1.11.5          | 205 KB    | ##################################### | 100% 
        cryptography-2.5     | 590 KB    | ##################################### | 100% 
        pycparser-2.19       | 173 KB    | ##################################### | 100% 
        Preparing transaction: done
        Verifying transaction: done
        Executing transaction: done
        (data_env) KANGs-MacBook-Pro:~ kang$ 


 
* 이제 jupyter notebook에서 pymysql import 사용 가능.

