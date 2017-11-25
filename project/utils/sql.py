#!/usr/bin/python
#Author:xiaojie
# -*- coding:utf-8 -*-

'''
#查看所有机器的系统
SELECT
  project_app_host.ip,
  project_app_system.name
FROM project_app_host
  LEFT JOIN project_app_system
    ON project_app_host.system_id = project_app_system.id AND project_app_system.name IN (SELECT project_app_system.name
                                                                                          FROM project_app_system);
'''

