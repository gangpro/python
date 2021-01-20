# Tensorflow
> google이 만든 머신러닝을 위한 library(python, c 언어로 구성)

<br>

## Tensorflow 설치
* 터미널 실행


        $ KANGs-MacBook-Pro ~ $ cd ~
          ↳ cd ~ : 최상위 폴더로 이동

* 가상환경 접속


        $ KANGs-MacBook-Pro ~ $ source activate data_env

* Tensorflow 설치


        $ KANGs-MacBook-Pro ~ $ conda install tensorflow
        Solving environment: done
        
        
        ==> WARNING: A newer version of conda exists. <==
          current version: 4.5.12
          latest version: 4.6.7
        
        Please update conda by running
        
            $ conda update -n base -c defaults conda
        
        
        
        ## Package Plan ##
        
          environment location: /anaconda3/envs/data_env
        
          added / updated specs: 
            - tensorflow
        
        
        The following packages will be downloaded:
        
            package                    |            build
            ---------------------------|-----------------
            keras-applications-1.0.6   |           py36_0          49 KB
            werkzeug-0.14.1            |           py36_0         423 KB
            markdown-3.0.1             |           py36_0         107 KB
            hdf5-1.10.4                |       hfa1e0ec_0         4.5 MB
            h5py-2.9.0                 |   py36h3134771_0         971 KB
            _tflow_select-2.3.0        |              mkl           3 KB
            gast-0.2.2                 |           py36_0         138 KB
            keras-preprocessing-1.0.5  |           py36_0          52 KB
            c-ares-1.15.0              |       h1de35cc_1          81 KB
            tensorflow-base-1.12.0     |mkl_py36h70e0e9a_0        85.6 MB
            astor-0.7.1                |           py36_0          43 KB
            absl-py-0.7.0              |           py36_0         156 KB
            tensorflow-1.12.0          |mkl_py36h2b2bbaf_0           4 KB
            grpcio-1.16.1              |   py36h044775b_1         944 KB
            libprotobuf-3.6.1          |       hd9629dc_0         3.8 MB
            protobuf-3.6.1             |   py36h0a44026_0         608 KB
            tensorboard-1.12.2         |   py36haf313ee_0         3.1 MB
            termcolor-1.1.0            |           py36_1           7 KB
            ------------------------------------------------------------
                                                   Total:       100.5 MB
        
        The following NEW packages will be INSTALLED:
        
            _tflow_select:       2.3.0-mkl                
            absl-py:             0.7.0-py36_0             
            astor:               0.7.1-py36_0             
            c-ares:              1.15.0-h1de35cc_1        
            gast:                0.2.2-py36_0             
            grpcio:              1.16.1-py36h044775b_1    
            h5py:                2.9.0-py36h3134771_0     
            hdf5:                1.10.4-hfa1e0ec_0        
            keras-applications:  1.0.6-py36_0             
            keras-preprocessing: 1.0.5-py36_0             
            libprotobuf:         3.6.1-hd9629dc_0         
            markdown:            3.0.1-py36_0             
            protobuf:            3.6.1-py36h0a44026_0     
            tensorboard:         1.12.2-py36haf313ee_0    
            tensorflow:          1.12.0-mkl_py36h2b2bbaf_0
            tensorflow-base:     1.12.0-mkl_py36h70e0e9a_0
            termcolor:           1.1.0-py36_1             
            werkzeug:            0.14.1-py36_0            
      
        
        Proceed ([y]/n)? y
         ↳ 설치를 원할 시 y 버튼을 클릭하고 엔터!
        
        
        Downloading and Extracting Packages
        keras-applications-1 | 49 KB     | ##################################### | 100% 
        werkzeug-0.14.1      | 423 KB    | ##################################### | 100% 
        markdown-3.0.1       | 107 KB    | ##################################### | 100% 
        hdf5-1.10.4          | 4.5 MB    | ##################################### | 100% 
        h5py-2.9.0           | 971 KB    | ##################################### | 100% 
        _tflow_select-2.3.0  | 3 KB      | ##################################### | 100% 
        gast-0.2.2           | 138 KB    | ##################################### | 100% 
        keras-preprocessing- | 52 KB     | ##################################### | 100% 
        c-ares-1.15.0        | 81 KB     | ##################################### | 100% 
        tensorflow-base-1.12 | 85.6 MB   | ##################################### | 100% 
        astor-0.7.1          | 43 KB     | ##################################### | 100% 
        absl-py-0.7.0        | 156 KB    | ##################################### | 100% 
        tensorflow-1.12.0    | 4 KB      | ##################################### | 100% 
        grpcio-1.16.1        | 944 KB    | ##################################### | 100% 
        libprotobuf-3.6.1    | 3.8 MB    | ##################################### | 100% 
        protobuf-3.6.1       | 608 KB    | ##################################### | 100% 
        tensorboard-1.12.2   | 3.1 MB    | ##################################### | 100% 
        termcolor-1.1.0      | 7 KB      | ##################################### | 100% 
        Preparing transaction: done
        Verifying transaction: done
        Executing transaction: done

 
* 이제 jupyter notebook에서 Tensorflow import 사용 가능.

