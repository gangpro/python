# scikit-learn
> 머신러닝 교육을 위한 파이썬 패키지

<br>

## sckit-learn 설치
* 터미널 실행


        $ KANGs-MacBook-Pro ~ $ cd ~
          ↳ cd ~ : 최상위 폴더로 이동

* 가상환경 접속


        $ KANGs-MacBook-Pro ~ $ source activate data_env

* scikit-learn 설치


        $ KANGs-MacBook-Pro ~ $ pip install sklearn
        Collecting sklearn
          Downloading https://files.pythonhosted.org/packages/1e/7a/dbb3be0ce9bd5c8b7e3d87328e79063f8b263b2b1bfa4774cb1147bfcd3f/sklearn-0.0.tar.gz
        Collecting scikit-learn (from sklearn)
          Downloading https://files.pythonhosted.org/packages/cb/5f/dfa0a118b8a503e45cd2cf48acb9cf1de8deaf06a3cef1b1c19bd5cbbc45/scikit_learn-0.20.2-cp36-cp36m-macosx_10_6_intel.macosx_10_9_intel.macosx_10_9_x86_64.macosx_10_10_intel.macosx_10_10_x86_64.whl (7.9MB)
            100% |████████████████████████████████| 7.9MB 3.3MB/s 
        Requirement already satisfied: numpy>=1.8.2 in /anaconda3/envs/data_env/lib/python3.6/site-packages (from scikit-learn->sklearn) (1.16.1)
        Requirement already satisfied: scipy>=0.13.3 in /anaconda3/envs/data_env/lib/python3.6/site-packages (from scikit-learn->sklearn) (1.2.1)
        Building wheels for collected packages: sklearn
          Building wheel for sklearn (setup.py) ... done
          Stored in directory: /Users/kang/Library/Caches/pip/wheels/76/03/bb/589d421d27431bcd2c6da284d5f2286c8e3b2ea3cf1594c074
        Successfully built sklearn
        Installing collected packages: scikit-learn, sklearn
        Successfully installed scikit-learn-0.20.2 sklearn-0.0

 
* 이제 jupyter notebook에서 scikit-learn import 사용 가능.

