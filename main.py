import sys

if sys.argv[-1] == "main.py":
    import randomyoutubevideo
    print(randomyoutubevideo.get_random_video_id())

if sys.argv[-1] == "clean":
    import shutil
    for i in ["build", "dist", "randomyoutubevideo.egg-info"]:
        shutil.rmtree(i)

if sys.argv[-1] == "build":
    import os
    os.system("python setup.py sdist bdist_wheel")

if sys.argv[-1] == "upload":
    import os
    os.system("twine upload dist/*")
