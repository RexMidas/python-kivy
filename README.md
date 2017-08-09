# python-kivy
python project for android app using docker as test env

# Setup test env using docker
docker search kivy

I used jlquant/docker-kivy because it mentioned android 

docker pull jlquant/docker-kivy

# To run test env
docker run -p 32788:6080 –d IMAGEID #replace IMAGEID with the image id found using "docker images" command

Go to your virtual machines IP with the port specified above, so in my case: 192.168.99.100:32788

# Get the sourcecode on the "Debian virtual machine" and run it
git clone https://github.com/RexMidas/python-kivy

cd python-kivy

python MainApp.py

# Deploy to android (first install buildozer on debian)
sudo pip install buildozer

buildozer init #creates a spec file

buildozer android debug deploy


# Developper Notes
- the python main class for android compilation should be main.py