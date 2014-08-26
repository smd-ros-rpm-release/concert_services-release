Name:           ros-indigo-concert-service-turtlesim
Version:        0.1.1
Release:        0%{?dist}
Summary:        ROS concert_service_turtlesim package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/concert_service_turtlesim
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-concert-service-msgs
Requires:       ros-indigo-concert-service-utilities
Requires:       ros-indigo-gateway-msgs
Requires:       ros-indigo-rocon-app-manager-msgs
Requires:       ros-indigo-rocon-console
Requires:       ros-indigo-rocon-gateway-utils
Requires:       ros-indigo-rocon-launch
Requires:       ros-indigo-rocon-python-comms
Requires:       ros-indigo-rocon-python-utils
Requires:       ros-indigo-rocon-std-msgs
Requires:       ros-indigo-rospy
Requires:       ros-indigo-std-msgs
Requires:       ros-indigo-turtlesim
BuildRequires:  ros-indigo-catkin

%description
Sets up the turtlesim engine as a service to assist in spawning/killing turtle
concert clients.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Tue Aug 26 2014 Daniel Stonier <d.stonier@gmail.com> - 0.1.1-0
- Autogenerated by Bloom

