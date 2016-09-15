__author__ = 'linglin'

class MyClass:

        def local(self, command):
                #return subprocess.call(command, shell=True)
                print "local"

        def sched_local(self, script_path, cron_definition):
                import schedule
                import time

                #job = self.local(script_path)

                schedule.every(1).minutes.do(self.local(), script_path)

                while True:
                        schedule.run_pending()
                        time.sleep(1)


if __name__ == "__main__":
    cg = MyClass()
    cg.sched_local("")