from nsbaseresource import NSBaseResource
__author__ = 'vlazarenko'


class NSLBMonitor(NSBaseResource):

        # Managing monitors for lb vservers
        def __init__(self, json_data=None):
                """
                Supplied with json_data the object can be pre-filled
                """
                super(NSLBMonitor, self).__init__()
                self.options = {'monitorname': '',
                                'alertretries': 0,
                                'destport': 0,
                                'downtime': 30,
                                'interval': '',
                                'lrtm': u'ENABLED',
                                'lrtmconf': 1,
                                'recv': 'OK',
                                'respcode': '200',
                                'resptimeout': 2,
                                'resptimeoutthresh': '0',
                                'retries': 3,
                                'reverse': 'NO',
                                'secure': 'NO',
                                'send': u'GET  /health-check/status-frontend-production-mfs',
                                'sipmethod': 'OPTIONS',
                                'snmpversion': 'V1',
                                'state': 'ENABLED',
                                'storedb': 'DISABLED',
                                'storefrontacctservice': 'NO',
                                'successretries': 1,
                                'tos': 'NO',
                                'transparent': 'NO',
                                'type': 'HTTP-ECV',
                                }

                self.resourcetype = NSLBMonitor.get_resourcetype()

                if not (json_data is None):
                        for key in json_data.keys():
                                if key in self.options.keys():
                                        self.options[key] = json_data[key]

        @staticmethod
        def get_resourcetype():
                return "lbmonitor"

        def set_monitorname(self, monitorname):
                self.options['monitorname'] = monitorname

        def get_monitorname(self):
                return self.options['monitorname']

        def set_recv(self, servicename):
                self.options['recv'] = servicename

        def get_recv(self):
                return self.options['recv']

        def set_send(self, send):
                self.options['send'] = send

        def get_send(self):
                return self.options['send']

        def set_secure(self, secure):
                self.options['secure'] = secure

        @staticmethod
        def get(nitro, monitor):
                """
                Use this API to fetch LB Monitor of given name.
                """
                __monitor = NSLBMonitor()
                __monitor.set_name(monitor.get_name())
                __monitor.get_resource(nitro)
                return __monitor
        
        def get_all(nitro):
                """
                Use this API to fetch all configured monitor resources.
                """
                
                __url = nitro.get_url() + NSLBMonitor.get_resourcetype()
                __json_servers = nitro.get(__url).get_response_field(NSLBMonitor.get_resourcetype())
                __monitors = []
                for json_monitor in __json_monitors:
                        __monitors.append(NSLBMonitor(json_monitor))
                return __servers
                
        def add(nitro, resource):
                """
                Use this API to add lbmonitor_service_binding.
                """
                __resource = NSLBMonitor()
                __resource.set_monitorname(resource.get_monitorname())
                __resource.set_servicename(resource.get_servicename())
                __resource.set_dup_state(resource.get_dup_state())
                __resource.set_dup_weight(resource.get_dup_weight())
                __resource.set_servicegroupname(resource.get_servicegroupname())
                __resource.set_state(resource.get_state())
                __resource.set_weight(resource.get_weight())
                return __resource.update_resource(nitro)
        
        @staticmethod
        def delete(nitro, resource):
                """
                Use this API to delete lbmonitor_service_binding of a given name.
                """
                __resource = NSLBMonitor()
                __resource.set_monitorname(resource.get_monitorname())
                __resource.set_servicename(resource.get_servicename())
                __resource.set_servicegroupname(resource.get_servicegroupname())
                nsresponse = __resource.delete_resource(nitro, object_name=__resource.get_monitorname())
                return nsresponse
                
                
