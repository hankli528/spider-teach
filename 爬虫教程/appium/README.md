官网：
http://appium.io

下载地址：
https://github.com/appium/appium-desktop/releases/tag/v1.8.2

linux,mac配置环境变量：
```
sudo vim /etc/hosts

export ANDROID_HOME=/Users/seancheney/Library/Android/sdk
export PATH=$ANDROID_HOME/platform-tools:$ANDROID_HOME/tools:$PATH
```


python安装appium api：
```
pip install Appium-Python-Client
```

adb查看设备名：
```
adb devices -l
```

adb命令查看包名：
```
adb shell pm list packages
```

package:com.miui.screenrecorder

package:com.android.cts.priv.ctsshim

package:com.qualcomm.qti.qms.service.telemetry

package:com.miui.contentextension



**查看appActivity**

1.cmd命令中输入：```adb shell``` 进入shell命令模式

2.shell中输入：```logcat | grep ActivityManager```   真机运行应用，可以实时 查看当前正在运行的Activity；

