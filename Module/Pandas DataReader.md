# Pandas DataReader
> Pandas DataReader Package<br>
> 웹 상의 데이터를 Pandas DataFrame 객체로 만드는 기능을 제공<br>

## **Pandas DataReader Package 설치**

* 터미널 실행


        $ KANGs-MacBook-Pro ~ $ cd ~
          ↳ cd ~ : 최상위 폴더로 이동

* 가상환경 접속


        $ KANGs-MacBook-Pro ~ $ source activate data_env

* pandas_datareader 설치


        $ (data_env) KANGs-MacBook-Pro:~ kang$ pip install pandas_datareader
        Collecting pandas_datareader
          Downloading https://files.pythonhosted.org/packages/cc/5c/ea5b6dcfd0f55c5fb1e37fb45335ec01cceca199b8a79339137f5ed269e0/pandas_datareader-0.7.0-py2.py3-none-any.whl (111kB)
            100% |████████████████████████████████| 112kB 1.3MB/s 
        Requirement already satisfied: pandas>=0.19.2 in /anaconda3/envs/data_env/lib/python3.6/site-packages (from pandas_datareader) (0.24.1)
        Collecting wrapt (from pandas_datareader)
          Downloading https://files.pythonhosted.org/packages/67/b2/0f71ca90b0ade7fad27e3d20327c996c6252a2ffe88f50a95bba7434eda9/wrapt-1.11.1.tar.gz
        Collecting requests>=2.3.0 (from pandas_datareader)
          Downloading https://files.pythonhosted.org/packages/7d/e3/20f3d364d6c8e5d2353c72a67778eb189176f08e873c9900e10c0287b84b/requests-2.21.0-py2.py3-none-any.whl (57kB)
            100% |████████████████████████████████| 61kB 4.6MB/s 
        Collecting lxml (from pandas_datareader)
          Downloading https://files.pythonhosted.org/packages/b5/5c/27b381a7d5b24ee4b9da1b02269a305bdc4fc30a3ea5bb21a5a98194850d/lxml-4.3.1-cp36-cp36m-macosx_10_6_intel.macosx_10_9_intel.macosx_10_9_x86_64.macosx_10_10_intel.macosx_10_10_x86_64.whl (8.8MB)
            100% |████████████████████████████████| 8.8MB 5.4MB/s 
        Requirement already satisfied: python-dateutil>=2.5.0 in /anaconda3/envs/data_env/lib/python3.6/site-packages (from pandas>=0.19.2->pandas_datareader) (2.7.5)
        Requirement already satisfied: numpy>=1.12.0 in /anaconda3/envs/data_env/lib/python3.6/site-packages (from pandas>=0.19.2->pandas_datareader) (1.16.1)
        Requirement already satisfied: pytz>=2011k in /anaconda3/envs/data_env/lib/python3.6/site-packages (from pandas>=0.19.2->pandas_datareader) (2018.9)
        Collecting urllib3<1.25,>=1.21.1 (from requests>=2.3.0->pandas_datareader)
          Downloading https://files.pythonhosted.org/packages/62/00/ee1d7de624db8ba7090d1226aebefab96a2c71cd5cfa7629d6ad3f61b79e/urllib3-1.24.1-py2.py3-none-any.whl (118kB)
            100% |████████████████████████████████| 122kB 3.1MB/s 
        Requirement already satisfied: certifi>=2017.4.17 in /anaconda3/envs/data_env/lib/python3.6/site-packages (from requests>=2.3.0->pandas_datareader) (2018.11.29)
        Requirement already satisfied: idna<2.9,>=2.5 in /anaconda3/envs/data_env/lib/python3.6/site-packages (from requests>=2.3.0->pandas_datareader) (2.8)
        Collecting chardet<3.1.0,>=3.0.2 (from requests>=2.3.0->pandas_datareader)
          Downloading https://files.pythonhosted.org/packages/bc/a9/01ffebfb562e4274b6487b4bb1ddec7ca55ec7510b22e4c51f14098443b8/chardet-3.0.4-py2.py3-none-any.whl (133kB)
            100% |████████████████████████████████| 143kB 19.2MB/s 
        Requirement already satisfied: six>=1.5 in /anaconda3/envs/data_env/lib/python3.6/site-packages (from python-dateutil>=2.5.0->pandas>=0.19.2->pandas_datareader) (1.12.0)
        Building wheels for collected packages: wrapt
          Building wheel for wrapt (setup.py) ... done
          Stored in directory: /Users/kang/Library/Caches/pip/wheels/89/67/41/63cbf0f6ac0a6156588b9587be4db5565f8c6d8ccef98202fc
        Successfully built wrapt
        Installing collected packages: wrapt, urllib3, chardet, requests, lxml, pandas-datareader
        Successfully installed chardet-3.0.4 lxml-4.3.1 pandas-datareader-0.7.0 requests-2.21.0 urllib3-1.24.1 wrapt-1.11.1

 
* 이제 jupyter notebook에서 pandas_datareader import 사용 가능.

