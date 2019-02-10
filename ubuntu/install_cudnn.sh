# Install cuDNN 5.1
#ubuntu_version="$(lsb_release -r)"
#CUDNN_URL="http://developer.download.nvidia.com/compute/redist/cudnn/v5.1/cudnn-9.1-linux-x64-v5.1.tgz"
#wget -c ${CUDNN_URL}
#sudo tar -xzf cudnn-9.1-linux-x64-v5.1.tgz -C /usr/local
#rm cudnn-9.1-linux-x64-v5.1.tgz && sudo ldconfig
#sudo dpkg --install libcudnn7-dev_7.7.2.24-1+cuda10.0_amd64.deb
sudo dpkg --install libcudnn7_7.1.3.16-1+cuda9.1_amd64.deb

