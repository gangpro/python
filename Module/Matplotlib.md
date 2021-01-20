# Matplotlib
> Matplotlib Library<br>
> plotting을 할 수 있는 python liblrary가 많이 있다. 그중 matplotlib <br>


## **Matplotlib Library**<br>

* 터미널 실행


        $ KANGs-MacBook-Pro ~ $ cd ~
          ↳ cd ~ : 최상위 폴더로 이동

* 가상환경 접속


        $ KANGs-MacBook-Pro ~ $ source activate data_env

* Matplotlib 설치


        $ KANGs-MacBook-Pro ~ $ conda install matplotlib
        Solving environment: done
        
        
        ==> WARNING: A newer version of conda exists. <==
          current version: 4.5.12
          latest version: 4.6.4
        
        Please update conda by running
        
            $ conda update -n base -c defaults conda
        
        
        
        ## Package Plan ##
        
          environment location: /anaconda3/envs/data_env
        
          added / updated specs: 
            - matplotlib
        
        
        The following packages will be downloaded:
        
            package                    |            build
            ---------------------------|-----------------
            libpng-1.6.36              |       ha441bb4_0         296 KB
            cycler-0.10.0              |   py36hfc81398_0          13 KB
            matplotlib-3.0.2           |   py36h54f8f79_0         6.5 MB
            kiwisolver-1.0.1           |   py36h0a44026_0          56 KB
            pyparsing-2.3.1            |           py36_0         105 KB
            ------------------------------------------------------------
                                                   Total:         7.0 MB
        
        The following NEW packages will be INSTALLED:
        
            cycler:     0.10.0-py36hfc81398_0
            freetype:   2.9.1-hb4e5f40_0     
            kiwisolver: 1.0.1-py36h0a44026_0 
            libpng:     1.6.36-ha441bb4_0    
            matplotlib: 3.0.2-py36h54f8f79_0 
            pyparsing:  2.3.1-py36_0         
        
        
        Proceed ([y]/n)? y
         ↳ 설치를 원할 시 y 버튼을 클릭하고 엔터!
        
        
        Downloading and Extracting Packages
        libpng-1.6.36        | 296 KB    | ##################################### | 100% 
        cycler-0.10.0        | 13 KB     | ##################################### | 100% 
        matplotlib-3.0.2     | 6.5 MB    | ##################################### | 100% 
        kiwisolver-1.0.1     | 56 KB     | ##################################### | 100% 
        pyparsing-2.3.1      | 105 KB    | ##################################### | 100% 
        Preparing transaction: done
        Verifying transaction: done
        Executing transaction: done
        
        (data_env) KANGs-MacBook-Pro:~ kang$ 

 
* 이제 jupyter notebook에서 Matplotlib import 사용 가능. 

