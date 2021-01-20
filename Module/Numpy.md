# NumPy
> NumPy Library<br>
> 행렬 연산을 위한 핵심 라이브러리<br>


## **NumPy Library**<br>

np는 Numerical Python의 약자(수치적인 처리를 하는 파이썬)(수치 계산에 특화, 1차원 백터, 다차원 매트릭스)
Vector(1차원 배열), Matrix(다차원 배열)연산에 상당한 편의성 제공
Pandas, matplotlib의 기반이 되는 library

Pandas Library(데이터분석을 하며, Pandas가 사용하는 자료구조를 NumPy이용)
matplotlib Library(데이터를 그림으로 표현할 때 사용)

자료가 구조가 딱 1개이다. 그건 바로, NumPy는 ndarray라는 배열을 사용
ndarray(n-dimension array) : 1차원 배열, 2차원 배열, 다차원 배열
배열의 가장 큰 특성은 같은 데이터 타입(data type)을 가진다는 것이다.
사용방법은 list와 거의 비슷하다. 하지만 실행속도면이나 메모리 용량 등에서 비교할 수 없이 좋다.



* 터미널 실행


        $ KANGs-MacBook-Pro ~ $ cd ~
          ↳ cd ~ : 최상위 폴더로 이동

* 가상환경 접속


        $ KANGs-MacBook-Pro ~ $ source activate data_env

* NumPy 설치


        $ KANGs-MacBook-Pro ~ $ conda install numpy
        Solving environment: done


        ==> WARNING: A newer version of conda exists. <==
          current version: 4.5.12
          latest version: 4.6.3
        
        Please update conda by running
        
            $ conda update -n base -c defaults conda



        ## Package Plan ##
        
          environment location: /anaconda3/envs/data_env
        
          added / updated specs: 
            - numpy
        
        
        The following packages will be downloaded:
        
            package                    |            build
            ---------------------------|-----------------
            mkl_fft-1.0.10             |   py36h5e564d8_0         156 KB
            mkl_random-1.0.2           |   py36h27c97d8_0         382 KB
            certifi-2018.11.29         |           py36_0         146 KB
            ca-certificates-2019.1.23  |                0         126 KB
            numpy-1.15.4               |   py36hacdab7b_0          47 KB
            numpy-base-1.15.4          |   py36h6575580_0         4.1 MB
            ------------------------------------------------------------
                                                   Total:         4.9 MB
        
        The following NEW packages will be INSTALLED:
        
            blas:            1.0-mkl                       
            intel-openmp:    2019.1-144                    
            libgfortran:     3.0.1-h93005f0_2              
            mkl:             2019.1-144                    
            mkl_fft:         1.0.10-py36h5e564d8_0         
            mkl_random:      1.0.2-py36h27c97d8_0          
            numpy:           1.15.4-py36hacdab7b_0         
            numpy-base:      1.15.4-py36h6575580_0         
        
        The following packages will be UPDATED:
        
            ca-certificates: 2019.1.23-0           anaconda --> 2019.1.23-0      
            certifi:         2018.11.29-py36_0     anaconda --> 2018.11.29-py36_0
        
        The following packages will be DOWNGRADED:
        
            openssl:         1.1.1-h1de35cc_0      anaconda --> 1.1.1a-h1de35cc_0
        
        
        Proceed ([y]/n)?  y																		<- y
         ↳ 설치를 원할 시 y 버튼을 클릭하고 엔터!
        
        
        Downloading and Extracting Packages
        mkl_fft-1.0.10       | 156 KB    | ##################################### | 100% 
        mkl_random-1.0.2     | 382 KB    | ##################################### | 100% 
        certifi-2018.11.29   | 146 KB    | ##################################### | 100% 
        ca-certificates-2019 | 126 KB    | ##################################### | 100% 
        numpy-1.15.4         | 47 KB     | ##################################### | 100% 
        numpy-base-1.15.4    | 4.1 MB    | ##################################### | 100% 
        Preparing transaction: done
        Verifying transaction: done
        Executing transaction: done

 
* 이제 jupyter notebook에서 넘파이 import 사용 가능.

