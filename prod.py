from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
import os
from daemon import runner

class AppDaemon():
    def __init__(self):
        current_folder = os.path.dirname(os.path.realpath(__file__))
        self.stdin_path = '/dev/null'
        self.stdout_path = '%s/pyblaster.out' % current_folder
        self.stderr_path = '%s/pyblaster.err' % current_folder
        self.pidfile_path = '%s/pyblaster.pid' % current_folder
        self.pidfile_timeout = 5

    def run(self):
        from web import app
        http_server = HTTPServer(WSGIContainer(app))
        http_server.listen(80)
        IOLoop.instance().start()


if __name__ == '__main__':
    app_daemon = AppDaemon()
    daemon_runner = runner.DaemonRunner(app_daemon)
    daemon_runner.do_action()
        


