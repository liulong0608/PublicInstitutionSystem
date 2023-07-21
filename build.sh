echo "运行容器python执行自动化"
#输出日志
#-w=$WORKSPACE：指定workspace
#--volumes-from=jenkins_save01：将jenkins容器中的workspace映射到python容器中，此时jenkins中git拉下来的代码就会被映射进去
docker run --rm -w=$WORKSPACE --volumes-from=jenkins_save01 python3.9:haili
echo "python执行自动化执行成功"
