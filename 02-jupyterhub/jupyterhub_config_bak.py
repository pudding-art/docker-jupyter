# Configuration file for jupyterhub.

c = get_config()  #noqa

#------------------------------------------------------------------------------
# Application(SingletonConfigurable) configuration
#------------------------------------------------------------------------------
## This is an application.

## The date format used by logging formatters for %(asctime)s
#  Default: '%Y-%m-%d %H:%M:%S'
# c.Application.log_datefmt = '%Y-%m-%d %H:%M:%S'

## The Logging format template
#  Default: '[%(name)s]%(highlevel)s %(message)s'
# c.Application.log_format = '[%(name)s]%(highlevel)s %(message)s'

## Set the log level by value or name.
#  Choices: any of [0, 10, 20, 30, 40, 50, 'DEBUG', 'INFO', 'WARN', 'ERROR', 'CRITICAL']
#  Default: 30
# c.Application.log_level = 30

## Configure additional log handlers.
#  
#  The default stderr logs handler is configured by the log_level, log_datefmt
#  and log_format settings.
#  
#  This configuration can be used to configure additional handlers (e.g. to
#  output the log to a file) or for finer control over the default handlers.
#  
#  If provided this should be a logging configuration dictionary, for more
#  information see:
#  https://docs.python.org/3/library/logging.config.html#logging-config-
#  dictschema
#  
#  This dictionary is merged with the base logging configuration which defines
#  the following:
#  
#  * A logging formatter intended for interactive use called
#    ``console``.
#  * A logging handler that writes to stderr called
#    ``console`` which uses the formatter ``console``.
#  * A logger with the name of this application set to ``DEBUG``
#    level.
#  
#  This example adds a new handler that writes to a file:
#  
#  .. code-block:: python
#  
#     c.Application.logging_config = {
#         "handlers": {
#             "file": {
#                 "class": "logging.FileHandler",
#                 "level": "DEBUG",
#                 "filename": "<path/to/file>",
#             }
#         },
#         "loggers": {
#             "<application-name>": {
#                 "level": "DEBUG",
#                 # NOTE: if you don't list the default "console"
#                 # handler here then it will be disabled
#                 "handlers": ["console", "file"],
#             },
#         },
#     }
#  Default: {}
# c.Application.logging_config = {}

## Instead of starting the Application, dump configuration to stdout
#  Default: False
# c.Application.show_config = False

## Instead of starting the Application, dump configuration to stdout (as JSON)
#  Default: False
# c.Application.show_config_json = False

#------------------------------------------------------------------------------
# JupyterHub(Application) configuration
#------------------------------------------------------------------------------
## An Application for starting a Multi-User Jupyter Notebook server.

## Maximum number of concurrent servers that can be active at a time.
#  
#  Setting this can limit the total resources your users can consume.
#  
#  An active server is any server that's not fully stopped. It is considered
#  active from the time it has been requested until the time that it has
#  completely stopped.
#  
#  If this many user servers are active, users will not be able to launch new
#  servers until a server is shutdown. Spawn requests will be rejected with a 429
#  error asking them to try again.
#  
#  If set to 0, no limit is enforced.
#  Default: 0
# c.JupyterHub.active_server_limit = 0

## Duration (in seconds) to determine the number of active users.
#  Default: 1800
# c.JupyterHub.active_user_window = 1800

## Resolution (in seconds) for updating activity
#  
#  If activity is registered that is less than activity_resolution seconds more
#  recent than the current value, the new value will be ignored.
#  
#  This avoids too many writes to the Hub database.
#  Default: 30
# c.JupyterHub.activity_resolution = 30

## DEPRECATED since version 2.0.0.
#  
#          The default admin role has full permissions, use custom RBAC scopes instead to
#          create restricted administrator roles.
#          https://jupyterhub.readthedocs.io/en/stable/rbac/index.html
#  Default: False
# c.JupyterHub.admin_access = False

## DEPRECATED since version 0.7.2, use Authenticator.admin_users instead.
#  Default: set()
# c.JupyterHub.admin_users = set()

## Allow named single-user servers per user
#  Default: False
# c.JupyterHub.allow_named_servers = False

## Answer yes to any questions (e.g. confirm overwrite)
#  Default: False
# c.JupyterHub.answer_yes = False

## The default amount of records returned by a paginated endpoint
#  Default: 50
# c.JupyterHub.api_page_default_limit = 50

## The maximum amount of records that can be returned at once
#  Default: 200
# c.JupyterHub.api_page_max_limit = 200

## PENDING DEPRECATION: consider using services
#  
#          Dict of token:username to be loaded into the database.
#  
#          Allows ahead-of-time generation of API tokens for use by externally managed services,
#          which authenticate as JupyterHub users.
#  
#          Consider using services for general services that talk to the
#  JupyterHub API.
#  Default: {}
# c.JupyterHub.api_tokens = {}

## Authentication for prometheus metrics
#  Default: True
# c.JupyterHub.authenticate_prometheus = True

## Class for authenticating users.
#  
#          This should be a subclass of :class:`jupyterhub.auth.Authenticator`
#  
#          with an :meth:`authenticate` method that:
#  
#          - is a coroutine (asyncio or tornado)
#          - returns username on success, None on failure
#          - takes two arguments: (handler, data),
#            where `handler` is the calling web.RequestHandler,
#            and `data` is the POST form data from the login page.
#  
#          .. versionchanged:: 1.0
#              authenticators may be registered via entry points,
#              e.g. `c.JupyterHub.authenticator_class = 'pam'`
#  
#  Currently installed: 
#    - default: jupyterhub.auth.PAMAuthenticator
#    - dummy: jupyterhub.auth.DummyAuthenticator
#    - null: jupyterhub.auth.NullAuthenticator
#    - pam: jupyterhub.auth.PAMAuthenticator
#    - shared-password: jupyterhub.authenticators.shared.SharedPasswordAuthenticator
#  Default: 'jupyterhub.auth.PAMAuthenticator'
# c.JupyterHub.authenticator_class = 'jupyterhub.auth.PAMAuthenticator'

## The base URL of the entire application.
#  
#          Add this to the beginning of all JupyterHub URLs.
#          Use base_url to run JupyterHub within an existing website.
#  Default: '/'
# c.JupyterHub.base_url = '/'

## The public facing URL of the whole JupyterHub application.
#  
#          This is the address on which the proxy will bind.
#          Sets protocol, ip, base_url
#  Default: 'http://:8000'
# c.JupyterHub.bind_url = 'http://:8000'

## Whether to shutdown the proxy when the Hub shuts down.
#  
#          Disable if you want to be able to teardown the Hub while leaving the
#  proxy running.
#  
#          Only valid if the proxy was starting by the Hub process.
#  
#          If both this and cleanup_servers are False, sending SIGINT to the Hub will
#          only shutdown the Hub, leaving everything else running.
#  
#          The Hub should be able to resume from database state.
#  Default: True
# c.JupyterHub.cleanup_proxy = True

## Whether to shutdown single-user servers when the Hub shuts down.
#  
#          Disable if you want to be able to teardown the Hub while leaving the
#  single-user servers running.
#  
#          If both this and cleanup_proxy are False, sending SIGINT to the Hub will
#          only shutdown the Hub, leaving everything else running.
#  
#          The Hub should be able to resume from database state.
#  Default: True
# c.JupyterHub.cleanup_servers = True

## Maximum number of concurrent users that can be spawning at a time.
#  
#  Spawning lots of servers at the same time can cause performance problems for
#  the Hub or the underlying spawning system. Set this limit to prevent bursts of
#  logins from attempting to spawn too many servers at the same time.
#  
#  This does not limit the number of total running servers. See
#  active_server_limit for that.
#  
#  If more than this many users attempt to spawn at a time, their requests will
#  be rejected with a 429 error asking them to try again. Users will have to wait
#  for some of the spawning services to finish starting before they can start
#  their own.
#  
#  If set to 0, no limit is enforced.
#  Default: 100
# c.JupyterHub.concurrent_spawn_limit = 100

## The config file to load
#  Default: 'jupyterhub_config.py'
# c.JupyterHub.config_file = 'jupyterhub_config.py'

## DEPRECATED: does nothing
#  Default: False
# c.JupyterHub.confirm_no_ssl = False

## Enable `__Host-` prefix on authentication cookies.
#  
#          The `__Host-` prefix on JupyterHub cookies provides further
#          protection against cookie tossing when untrusted servers
#          may control subdomains of your jupyterhub deployment.
#  
#          _However_, it also requires that cookies be set on the path `/`,
#          which means they are shared by all JupyterHub components,
#          so a compromised server component will have access to _all_ JupyterHub-related
#          cookies of the visiting browser.
#          It is recommended to only combine `__Host-` cookies with per-user domains.
#  
#          .. versionadded:: 4.1
#  Default: False
# c.JupyterHub.cookie_host_prefix_enabled = False

## Number of days for a login cookie to be valid.
#          Default is two weeks.
#  Default: 14
# c.JupyterHub.cookie_max_age_days = 14

## The cookie secret to use to encrypt cookies.
#  
#          Loaded from the JPY_COOKIE_SECRET env variable by default.
#  
#          Should be exactly 256 bits (32 bytes).
#  Default: traitlets.Undefined
# c.JupyterHub.cookie_secret = traitlets.Undefined

## File in which to store the cookie secret.
#  Default: 'jupyterhub_cookie_secret'
# c.JupyterHub.cookie_secret_file = 'jupyterhub_cookie_secret'

## Custom scopes to define.
#  
#          For use when defining custom roles,
#          to grant users granular permissions
#  
#          All custom scopes must have a description,
#          and must start with the prefix `custom:`.
#  
#          For example::
#  
#              custom_scopes = {
#                  "custom:jupyter_server:read": {
#                      "description": "read-only access to a single-user server",
#                  },
#              }
#  Default: {}
# c.JupyterHub.custom_scopes = {}

## The location of jupyterhub data files (e.g. /usr/local/share/jupyterhub)
#  Default: '/Users/hong/opt/anaconda3/envs/hta_new/share/jupyterhub'
# c.JupyterHub.data_files_path = '/Users/hong/opt/anaconda3/envs/hta_new/share/jupyterhub'

## Include any kwargs to pass to the database connection.
#          See sqlalchemy.create_engine for details.
#  Default: {}
# c.JupyterHub.db_kwargs = {}

## url for the database. e.g. `sqlite:///jupyterhub.sqlite`
#  Default: 'sqlite:///jupyterhub.sqlite'
# c.JupyterHub.db_url = 'sqlite:///jupyterhub.sqlite'

## log all database transactions. This has A LOT of output
#  Default: False
# c.JupyterHub.debug_db = False

## DEPRECATED since version 0.8: Use ConfigurableHTTPProxy.debug
#  Default: False
# c.JupyterHub.debug_proxy = False

## If named servers are enabled, default name of server to spawn or open when no
#  server is specified, e.g. by user-redirect.
#  
#  Note: This has no effect if named servers are not enabled, and does _not_
#  change the existence or behavior of the default server named `''` (the empty
#  string). This only affects which named server is launched when no server is
#  specified, e.g. by links to `/hub/user-redirect/lab/tree/mynotebook.ipynb`.
#  Default: ''
# c.JupyterHub.default_server_name = ''

## The default URL for users when they arrive (e.g. when user directs to "/")
#  
#  By default, redirects users to their own server.
#  
#  Can be a Unicode string (e.g. '/hub/home') or a callable based on the handler
#  object:
#  
#  ::
#  
#      def default_url_fn(handler):
#          user = handler.current_user
#          if user and user.admin:
#              return '/hub/admin'
#          return '/hub/home'
#  
#      c.JupyterHub.default_url = default_url_fn
#  Default: traitlets.Undefined
# c.JupyterHub.default_url = traitlets.Undefined

## Dict authority:dict(files). Specify the key, cert, and/or
#          ca file for an authority. This is useful for externally managed
#          proxies that wish to use internal_ssl.
#  
#          The files dict has this format (you must specify at least a cert)::
#  
#              {
#                  'key': '/path/to/key.key',
#                  'cert': '/path/to/cert.crt',
#                  'ca': '/path/to/ca.crt'
#              }
#  
#          The authorities you can override: 'hub-ca', 'notebooks-ca',
#          'proxy-api-ca', 'proxy-client-ca', and 'services-ca'.
#  
#          Use with internal_ssl
#  Default: {}
# c.JupyterHub.external_ssl_authorities = {}

## DEPRECATED.
#  
#  If you need to register additional HTTP endpoints please use services instead.
#  Default: []
# c.JupyterHub.extra_handlers = []

## DEPRECATED: use output redirection instead, e.g.
#  
#  jupyterhub &>> /var/log/jupyterhub.log
#  Default: ''
# c.JupyterHub.extra_log_file = ''

## Extra log handlers to set on JupyterHub logger
#  Default: []
# c.JupyterHub.extra_log_handlers = []

## Alternate header to use as the Host (e.g., X-Forwarded-Host)
#          when determining whether a request is cross-origin
#  
#          This may be useful when JupyterHub is running behind a proxy that rewrites
#          the Host header.
#  Default: ''
# c.JupyterHub.forwarded_host_header = ''

## Generate certs used for internal ssl
#  Default: False
# c.JupyterHub.generate_certs = False

## Generate default config file
#  Default: False
# c.JupyterHub.generate_config = False

## The URL on which the Hub will listen. This is a private URL for internal
#  communication. Typically set in combination with hub_connect_url. If a unix
#  socket, hub_connect_url **must** also be set.
#  
#  For example:
#  
#      "http://127.0.0.1:8081"
#      "unix+http://%2Fsrv%2Fjupyterhub%2Fjupyterhub.sock"
#  
#  .. versionadded:: 0.9
#  Default: ''
# c.JupyterHub.hub_bind_url = ''

## The ip or hostname for proxies and spawners to use
#          for connecting to the Hub.
#  
#          Use when the bind address (`hub_ip`) is 0.0.0.0, :: or otherwise different
#          from the connect address.
#  
#          Default: when `hub_ip` is 0.0.0.0 or ::, use `socket.gethostname()`,
#  otherwise use `hub_ip`.
#  
#          Note: Some spawners or proxy implementations might not support hostnames. Check your
#          spawner or proxy documentation to see if they have extra requirements.
#  
#          .. versionadded:: 0.8
#  Default: ''
# c.JupyterHub.hub_connect_ip = ''

## DEPRECATED
#  
#  Use hub_connect_url
#  
#  .. versionadded:: 0.8
#  
#  .. deprecated:: 0.9
#      Use hub_connect_url
#  Default: 0
# c.JupyterHub.hub_connect_port = 0

## The URL for connecting to the Hub. Spawners, services, and the proxy will use
#  this URL to talk to the Hub.
#  
#  Only needs to be specified if the default hub URL is not connectable (e.g.
#  using a unix+http:// bind url).
#  
#  .. seealso::
#      JupyterHub.hub_connect_ip
#      JupyterHub.hub_bind_url
#  
#  .. versionadded:: 0.9
#  Default: ''
# c.JupyterHub.hub_connect_url = ''

## The ip address for the Hub process to *bind* to.
#  
#          By default, the hub listens on localhost only. This address must be accessible from
#          the proxy and user servers. You may need to set this to a public ip or '' for all
#          interfaces if the proxy or user servers are in containers or on a different host.
#  
#          See `hub_connect_ip` for cases where the bind and connect address should differ,
#          or `hub_bind_url` for setting the full bind URL.
#  Default: '127.0.0.1'
# c.JupyterHub.hub_ip = '127.0.0.1'

## The internal port for the Hub process.
#  
#          This is the internal port of the hub itself. It should never be accessed directly.
#          See JupyterHub.port for the public port to use when accessing jupyterhub.
#          It is rare that this port should be set except in cases of port conflict.
#  
#          See also `hub_ip` for the ip and `hub_bind_url` for setting the full
#  bind URL.
#  Default: 8081
# c.JupyterHub.hub_port = 8081

## The routing prefix for the Hub itself.
#  
#  Override to send only a subset of traffic to the Hub. Default is to use the
#  Hub as the default route for all requests.
#  
#  This is necessary for normal jupyterhub operation, as the Hub must receive
#  requests for e.g. `/user/:name` when the user's server is not running.
#  
#  However, some deployments using only the JupyterHub API may want to handle
#  these events themselves, in which case they can register their own default
#  target with the proxy and set e.g. `hub_routespec = /hub/` to serve only the
#  hub's own pages, or even `/hub/api/` for api-only operation.
#  
#  Note: hub_routespec must include the base_url, if any.
#  
#  .. versionadded:: 1.4
#  Default: '/'
# c.JupyterHub.hub_routespec = '/'

## Trigger implicit spawns after this many seconds.
#  
#          When a user visits a URL for a server that's not running,
#          they are shown a page indicating that the requested server
#          is not running with a button to spawn the server.
#  
#          Setting this to a positive value will redirect the user
#          after this many seconds, effectively clicking this button
#          automatically for the users,
#          automatically beginning the spawn process.
#  
#          Warning: this can result in errors and surprising behavior
#          when sharing access URLs to actual servers,
#          since the wrong server is likely to be started.
#  Default: 0
# c.JupyterHub.implicit_spawn_seconds = 0

## Timeout (in seconds) to wait for spawners to initialize
#  
#  Checking if spawners are healthy can take a long time if many spawners are
#  active at hub start time.
#  
#  If it takes longer than this timeout to check, init_spawner will be left to
#  complete in the background and the http server is allowed to start.
#  
#  A timeout of -1 means wait forever, which can mean a slow startup of the Hub
#  but ensures that the Hub is fully consistent by the time it starts responding
#  to requests. This matches the behavior of jupyterhub 1.0.
#  
#  .. versionadded: 1.1.0
#  Default: 10
# c.JupyterHub.init_spawners_timeout = 10

## The location to store certificates automatically created by
#          JupyterHub.
#  
#          Use with internal_ssl
#  Default: 'internal-ssl'
# c.JupyterHub.internal_certs_location = 'internal-ssl'

## Enable SSL for all internal communication
#  
#          This enables end-to-end encryption between all JupyterHub components.
#          JupyterHub will automatically create the necessary certificate
#          authority and sign notebook certificates as they're created.
#  Default: False
# c.JupyterHub.internal_ssl = False

## The public facing ip of the whole JupyterHub application
#          (specifically referred to as the proxy).
#  
#          This is the address on which the proxy will listen. The default is to
#          listen on all interfaces. This is the only address through which JupyterHub
#          should be accessed by users.
#  Default: ''
# c.JupyterHub.ip = ''

## Supply extra arguments that will be passed to Jinja environment.
#  Default: {}
# c.JupyterHub.jinja_environment_options = {}

## Interval (in seconds) at which to update last-activity timestamps.
#  Default: 300
# c.JupyterHub.last_activity_interval = 300

## Dict of `{'group': {'users':['usernames'], 'properties': {}}`  to load at
#  startup.
#  
#  Example::
#  
#      c.JupyterHub.load_groups = {
#          'groupname': {
#              'users': ['usernames'],
#              'properties': {'key': 'value'},
#          },
#      }
#  
#  This strictly *adds* groups and users to groups. Properties, if defined,
#  replace all existing properties.
#  
#  Loading one set of groups, then starting JupyterHub again with a different set
#  will not remove users or groups from previous launches. That must be done
#  through the API.
#  
#  .. versionchanged:: 3.2
#    Changed format of group from list of usernames to dict
#  Default: {}
# c.JupyterHub.load_groups = {}

## List of predefined role dictionaries to load at startup.
#  
#          For instance::
#  
#              load_roles = [
#                              {
#                                  'name': 'teacher',
#                                  'description': 'Access to users' information and group membership',
#                                  'scopes': ['users', 'groups'],
#                                  'users': ['cyclops', 'gandalf'],
#                                  'services': [],
#                                  'groups': []
#                              }
#                          ]
#  
#          All keys apart from 'name' are optional.
#          See all the available scopes in the JupyterHub REST API documentation.
#  
#          Default roles are defined in roles.py.
#  Default: []
# c.JupyterHub.load_roles = []

## The date format used by logging formatters for %(asctime)s
#  See also: Application.log_datefmt
# c.JupyterHub.log_datefmt = '%Y-%m-%d %H:%M:%S'

## The Logging format template
#  See also: Application.log_format
# c.JupyterHub.log_format = '[%(name)s]%(highlevel)s %(message)s'

## Set the log level by value or name.
#  See also: Application.log_level
# c.JupyterHub.log_level = 30

## 
#  See also: Application.logging_config
# c.JupyterHub.logging_config = {}

## Specify path to a logo image to override the Jupyter logo in the banner.
#  Default: ''
# c.JupyterHub.logo_file = ''

## Maximum number of concurrent named servers that can be created by a user at a
#  time.
#  
#  Setting this can limit the total resources a user can consume.
#  
#  If set to 0, no limit is enforced.
#  
#  Can be an integer or a callable/awaitable based on the handler object:
#  
#  ::
#  
#      def named_server_limit_per_user_fn(handler):
#          user = handler.current_user
#          if user and user.admin:
#              return 0
#          return 5
#  
#      c.JupyterHub.named_server_limit_per_user = named_server_limit_per_user_fn
#  Default: 0
# c.JupyterHub.named_server_limit_per_user = 0

## Expiry (in seconds) of OAuth access tokens.
#  
#          The default is to expire when the cookie storing them expires,
#          according to `cookie_max_age_days` config.
#  
#          These are the tokens stored in cookies when you visit
#          a single-user server or service.
#          When they expire, you must re-authenticate with the Hub,
#          even if your Hub authentication is still valid.
#          If your Hub authentication is valid,
#          logging in may be a transparent redirect as you refresh the page.
#  
#          This does not affect JupyterHub API tokens in general,
#          which do not expire by default.
#          Only tokens issued during the oauth flow
#          accessing services and single-user servers are affected.
#  
#          .. versionadded:: 1.4
#              OAuth token expires_in was not previously configurable.
#          .. versionchanged:: 1.4
#              Default now uses cookie_max_age_days so that oauth tokens
#              which are generally stored in cookies,
#              expire when the cookies storing them expire.
#              Previously, it was one hour.
#  Default: 0
# c.JupyterHub.oauth_token_expires_in = 0

## File to write PID
#          Useful for daemonizing JupyterHub.
#  Default: ''
# c.JupyterHub.pid_file = ''

## The public facing port of the proxy.
#  
#          This is the port on which the proxy will listen.
#          This is the only port through which JupyterHub
#          should be accessed by users.
#  Default: 8000
# c.JupyterHub.port = 8000

## DEPRECATED since version 0.8 : Use ConfigurableHTTPProxy.api_url
#  Default: ''
# c.JupyterHub.proxy_api_ip = ''

## DEPRECATED since version 0.8 : Use ConfigurableHTTPProxy.api_url
#  Default: 0
# c.JupyterHub.proxy_api_port = 0

## DEPRECATED since version 0.8: Use ConfigurableHTTPProxy.auth_token
#  Default: ''
# c.JupyterHub.proxy_auth_token = ''

## DEPRECATED since version 0.8: Use ConfigurableHTTPProxy.check_running_interval
#  Default: 5
# c.JupyterHub.proxy_check_interval = 5

## The class to use for configuring the JupyterHub proxy.
#  
#          Should be a subclass of :class:`jupyterhub.proxy.Proxy`.
#  
#          .. versionchanged:: 1.0
#              proxies may be registered via entry points,
#              e.g. `c.JupyterHub.proxy_class = 'traefik'`
#  
#  Currently installed: 
#    - configurable-http-proxy: jupyterhub.proxy.ConfigurableHTTPProxy
#    - default: jupyterhub.proxy.ConfigurableHTTPProxy
#  Default: 'jupyterhub.proxy.ConfigurableHTTPProxy'
# c.JupyterHub.proxy_class = 'jupyterhub.proxy.ConfigurableHTTPProxy'

## DEPRECATED since version 0.8. Use ConfigurableHTTPProxy.command
#  Default: []
# c.JupyterHub.proxy_cmd = []

## Set the public URL of JupyterHub
#  
#          This will skip any detection of URL and protocol from requests,
#          which isn't always correct when JupyterHub is behind
#          multiple layers of proxies, etc.
#          Usually the failure is detecting http when it's really https.
#  
#          Should include the full, public URL of JupyterHub,
#          including the public-facing base_url prefix
#          (i.e. it should include a trailing slash), e.g.
#          https://jupyterhub.example.org/prefix/
#  Default: ''
# c.JupyterHub.public_url = ''

## Recreate all certificates used within JupyterHub on restart.
#  
#          Note: enabling this feature requires restarting all notebook servers.
#  
#          Use with internal_ssl
#  Default: False
# c.JupyterHub.recreate_internal_certs = False

## Redirect user to server (if running), instead of control panel.
#  Default: True
# c.JupyterHub.redirect_to_server = True

## Purge and reset the database.
#  Default: False
# c.JupyterHub.reset_db = False

## Interval (in seconds) at which to check connectivity of services with web
#  endpoints.
#  Default: 60
# c.JupyterHub.service_check_interval = 60

## Dict of token:servicename to be loaded into the database.
#  
#          Allows ahead-of-time generation of API tokens for use by externally
#  managed services.
#  Default: {}
# c.JupyterHub.service_tokens = {}

## List of service specification dictionaries.
#  
#          A service
#  
#          For instance::
#  
#              services = [
#                  {
#                      'name': 'cull_idle',
#                      'command': ['/path/to/cull_idle_servers.py'],
#                  },
#                  {
#                      'name': 'formgrader',
#                      'url': 'http://127.0.0.1:1234',
#                      'api_token': 'super-secret',
#                      'environment':
#                  }
#              ]
#  Default: []
# c.JupyterHub.services = []

## Instead of starting the Application, dump configuration to stdout
#  See also: Application.show_config
# c.JupyterHub.show_config = False

## Instead of starting the Application, dump configuration to stdout (as JSON)
#  See also: Application.show_config_json
# c.JupyterHub.show_config_json = False

## Shuts down all user servers on logout
#  Default: False
# c.JupyterHub.shutdown_on_logout = False

## The class to use for spawning single-user servers.
#  
#          Should be a subclass of :class:`jupyterhub.spawner.Spawner`.
#  
#          .. versionchanged:: 1.0
#              spawners may be registered via entry points,
#              e.g. `c.JupyterHub.spawner_class = 'localprocess'`
#  
#  Currently installed: 
#    - default: jupyterhub.spawner.LocalProcessSpawner
#    - localprocess: jupyterhub.spawner.LocalProcessSpawner
#    - simple: jupyterhub.spawner.SimpleLocalProcessSpawner
#  Default: 'jupyterhub.spawner.LocalProcessSpawner'
# c.JupyterHub.spawner_class = 'jupyterhub.spawner.LocalProcessSpawner'

## Path to SSL certificate file for the public facing interface of the proxy
#  
#          When setting this, you should also set ssl_key
#  Default: ''
# c.JupyterHub.ssl_cert = ''

## Path to SSL key file for the public facing interface of the proxy
#  
#          When setting this, you should also set ssl_cert
#  Default: ''
# c.JupyterHub.ssl_key = ''

## Host to send statsd metrics to. An empty string (the default) disables sending
#  metrics.
#  Default: ''
# c.JupyterHub.statsd_host = ''

## Port on which to send statsd metrics about the hub
#  Default: 8125
# c.JupyterHub.statsd_port = 8125

## Prefix to use for all metrics sent by jupyterhub to statsd
#  Default: 'jupyterhub'
# c.JupyterHub.statsd_prefix = 'jupyterhub'

## Hook for constructing subdomains for users and services. Only used when
#  `JupyterHub.subdomain_host` is set.
#  
#  There are two predefined hooks, which can be selected by name:
#  
#  - 'legacy' (deprecated) - 'idna' (default, more robust. No change for _most_
#  usernames)
#  
#  Otherwise, should be a function which must not be async. A custom
#  subdomain_hook should have the signature:
#  
#  def subdomain_hook(name, domain, kind) -> str:
#      ...
#  
#  and should return a unique, valid domain name for all usernames.
#  
#  - `name` is the original name, which may need escaping to be safe as a domain
#  name label - `domain` is the domain of the Hub itself - `kind` will be one of
#  'user' or 'service'
#  
#  JupyterHub itself puts very little limit on usernames to accommodate a wide
#  variety of Authenticators, but your identity provider is likely much more
#  strict, allowing you to make assumptions about the name.
#  
#  The 'idna' hook should produce a valid domain name for any user, using IDNA
#  encoding for unicode usernames, and a truncate-and-hash approach for any
#  usernames that can't be easily encoded into a domain component.
#  
#  .. versionadded:: 5.0
#  Default: 'idna'
# c.JupyterHub.subdomain_hook = 'idna'

## Run single-user servers on subdomains of this host.
#  
#          This should be the full `https://hub.domain.tld[:port]`.
#  
#          Provides additional cross-site protections for javascript served by
#  single-user servers.
#  
#          Requires `<username>.hub.domain.tld` to resolve to the same host as
#  `hub.domain.tld`.
#  
#          In general, this is most easily achieved with wildcard DNS.
#  
#          When using SSL (i.e. always) this also requires a wildcard SSL
#  certificate.
#  Default: ''
# c.JupyterHub.subdomain_host = ''

## Paths to search for jinja templates, before using the default templates.
#  Default: []
# c.JupyterHub.template_paths = []

## Extra variables to be passed into jinja templates.
#  
#          Values in dict may contain callable objects.
#          If value is callable, the current user is passed as argument.
#  
#          Example::
#  
#              def callable_value(user):
#                  # user is generated by handlers.base.get_current_user
#                  with open("/tmp/file.txt", "r") as f:
#                      ret = f.read()
#                  ret = ret.replace("<username>", user.name)
#                  return ret
#  
#              c.JupyterHub.template_vars = {
#                  "key1": "value1",
#                  "key2": callable_value,
#              }
#  Default: {}
# c.JupyterHub.template_vars = {}

## Set the maximum expiration (in seconds) of tokens created via the API.
#  
#  Set to any positive value to disallow creation of tokens with no expiration.
#  
#  0 (default) = no limit.
#  
#  Does not affect:
#  
#  - Server API tokens ($JUPYTERHUB_API_TOKEN is tied to lifetime of the server)
#  - Tokens issued during oauth (use `oauth_token_expires_in`) - Tokens created
#  via the API before configuring this limit
#  
#  .. versionadded:: 5.1
#  Default: 0
# c.JupyterHub.token_expires_in_max_seconds = 0

## Extra settings overrides to pass to the tornado application.
#  Default: {}
# c.JupyterHub.tornado_settings = {}

## Trust user-provided tokens (via JupyterHub.service_tokens)
#          to have good entropy.
#  
#          If you are not inserting additional tokens via configuration file,
#          this flag has no effect.
#  
#          In JupyterHub 0.8, internally generated tokens do not
#          pass through additional hashing because the hashing is costly
#          and does not increase the entropy of already-good UUIDs.
#  
#          User-provided tokens, on the other hand, are not trusted to have good entropy by default,
#          and are passed through many rounds of hashing to stretch the entropy of the key
#          (i.e. user-provided tokens are treated as passwords instead of random keys).
#          These keys are more costly to check.
#  
#          If your inserted tokens are generated by a good-quality mechanism,
#          e.g. `openssl rand -hex 32`, then you can set this flag to True
#          to reduce the cost of checking authentication tokens.
#  Default: False
# c.JupyterHub.trust_user_provided_tokens = False

## Names to include in the subject alternative name.
#  
#          These names will be used for server name verification. This is useful
#          if JupyterHub is being run behind a reverse proxy or services using ssl
#          are on different hosts.
#  
#          Use with internal_ssl
#  Default: []
# c.JupyterHub.trusted_alt_names = []

## Downstream proxy IP addresses to trust.
#  
#          This sets the list of IP addresses that are trusted and skipped when processing
#          the `X-Forwarded-For` header. For example, if an external proxy is used for TLS
#          termination, its IP address should be added to this list to ensure the correct
#          client IP addresses are recorded in the logs instead of the proxy server's IP
#          address.
#  Default: []
# c.JupyterHub.trusted_downstream_ips = []

## Upgrade the database automatically on start.
#  
#          Only safe if database is regularly backed up.
#          Only SQLite databases will be backed up to a local file automatically.
#  Default: False
# c.JupyterHub.upgrade_db = False

## Return 503 rather than 424 when request comes in for a non-running server.
#  
#  Prior to JupyterHub 2.0, we returned a 503 when any request came in for a user
#  server that was currently not running. By default, JupyterHub 2.0 will return
#  a 424 - this makes operational metric dashboards more useful.
#  
#  JupyterLab < 3.2 expected the 503 to know if the user server is no longer
#  running, and prompted the user to start their server. Set this config to true
#  to retain the old behavior, so JupyterLab < 3.2 can continue to show the
#  appropriate UI when the user server is stopped.
#  
#  This option will be removed in a future release.
#  Default: False
# c.JupyterHub.use_legacy_stopped_server_status_code = False

## Callable to affect behavior of /user-redirect/
#  
#  Receives 4 parameters: 1. path - URL path that was provided after /user-
#  redirect/ 2. request - A Tornado HTTPServerRequest representing the current
#  request. 3. user - The currently authenticated user. 4. base_url - The
#  base_url of the current hub, for relative redirects
#  
#  It should return the new URL to redirect to, or None to preserve current
#  behavior.
#  Default: None
# c.JupyterHub.user_redirect_hook = None

#------------------------------------------------------------------------------
# Authenticator(LoggingConfigurable) configuration
#------------------------------------------------------------------------------
## Base class for implementing an authentication provider for JupyterHub

## Set of users that will be granted admin rights on this JupyterHub.
#  
#  Note:
#  
#      As of JupyterHub 2.0,
#      full admin rights should not be required,
#      and more precise permissions can be managed via roles.
#  
#  Caution:
#  
#      Adding users to `admin_users` can only *grant* admin rights,
#      removing a username from the admin_users set **DOES NOT** remove admin rights previously granted.
#  
#      For an authoritative, restricted set of admins,
#      assign explicit membership of the `admin` *role*::
#  
#          c.JupyterHub.load_roles = [
#              {
#                  "name": "admin",
#                  "users": ["admin1", "..."],
#              }
#          ]
#  
#  Admin users can take every possible action on behalf of all users, for
#  example:
#  
#  - Use the admin panel to see list of users logged in - Add / remove users in
#  some authenticators - Restart / halt the hub - Start / stop users' single-user
#  servers - Can access each individual users' single-user server
#  
#  Admin access should be treated the same way root access is.
#  
#  Defaults to an empty set, in which case no user has admin access.
#  Default: set()
# c.Authenticator.admin_users = set()

## Allow every user who can successfully authenticate to access JupyterHub.
#  
#  False by default, which means for most Authenticators, _some_ allow-related
#  configuration is required to allow users to log in.
#  
#  Authenticator subclasses may override the default with e.g.::
#  
#      from traitlets import default
#      @default("allow_all")
#      def _default_allow_all(self):
#          # if _any_ auth config (depends on the Authenticator)
#          if self.allowed_users or self.allowed_groups or self.allow_existing_users:
#              return False
#          else:
#              return True
#  
#  .. versionadded:: 5.0
#  
#  .. versionchanged:: 5.0
#      Prior to 5.0, `allow_all` wasn't defined on its own,
#      and was instead implicitly True when no allow config was provided,
#      i.e. `allowed_users` unspecified or empty on the base Authenticator class.
#  
#      To preserve pre-5.0 behavior,
#      set `allow_all = True` if you have no other allow configuration.
#  Default: False
# c.Authenticator.allow_all = False

## Allow existing users to login.
#  
#  Defaults to True if `allowed_users` is set for historical reasons, and False
#  otherwise.
#  
#  With this enabled, all users present in the JupyterHub database are allowed to
#  login. This has the effect of any user who has _previously_ been allowed to
#  login via any means will continue to be allowed until the user is deleted via
#  the /hub/admin page or REST API.
#  
#  .. warning::
#  
#     Before enabling this you should review the existing users in the
#     JupyterHub admin panel at `/hub/admin`. You may find users existing
#     there because they have previously been declared in config such as
#     `allowed_users` or allowed to sign in.
#  
#  .. warning::
#  
#     When this is enabled and you wish to remove access for one or more
#     users previously allowed, you must make sure that they
#     are removed from the jupyterhub database. This can be tricky to do
#     if you stop allowing an externally managed group of users for example.
#  
#  With this enabled, JupyterHub admin users can visit `/hub/admin` or use
#  JupyterHub's REST API to add and remove users to manage who can login.
#  
#  .. versionadded:: 5.0
#  Default: False
# c.Authenticator.allow_existing_users = False

## Set of usernames that are allowed to log in.
#  
#  Use this to limit which authenticated users may login. Default behavior: only
#  users in this set are allowed.
#  
#  If empty, does not perform any restriction, in which case any authenticated
#  user is allowed.
#  
#  Authenticators may extend :meth:`.Authenticator.check_allowed` to combine
#  `allowed_users` with other configuration to either expand or restrict access.
#  
#  .. versionchanged:: 1.2
#      `Authenticator.whitelist` renamed to `allowed_users`
#  Default: set()
# c.Authenticator.allowed_users = set()

## Is there any allow config?
#  
#          Used to show a warning if it looks like nobody can access the Hub,
#          which can happen when upgrading to JupyterHub 5,
#          now that `allow_all` defaults to False.
#  
#          Deployments can set this explicitly to True to suppress
#          the "No allow config found" warning.
#  
#          Will be True if any config tagged with `.tag(allow_config=True)`
#          or starts with `allow` is truthy.
#  
#          .. versionadded:: 5.0
#  Default: False
# c.Authenticator.any_allow_config = False

## The max age (in seconds) of authentication info
#          before forcing a refresh of user auth info.
#  
#          Authenticators that support it may re-load managed groups,
#          refresh auth tokens, etc., or force a new login if auth info cannot be refreshed.
#  
#          See :meth:`.refresh_user` for what happens when user auth info is refreshed,
#          which varies by authenticator.
#          If an Authenticator does not implement `refresh_user`,
#          auth info will never be considered stale.
#  
#          Set `auth_refresh_age = 0` to disable time-based calls to `refresh_user`.
#          You can still use :attr:`refresh_pre_spawn` if `auth_refresh_age` is disabled.
#  Default: 300
# c.Authenticator.auth_refresh_age = 300

## Automatically begin the login process
#  
#          rather than starting with a "Login with..." link at `/hub/login`
#  
#          To work, `.login_url()` must give a URL other than the default `/hub/login`,
#          such as an oauth handler or another automatic login handler,
#          registered with `.get_handlers()`.
#  
#          .. versionadded:: 0.8
#  Default: False
# c.Authenticator.auto_login = False

## Automatically begin login process for OAuth2 authorization requests
#  
#  When another application is using JupyterHub as OAuth2 provider, it sends
#  users to `/hub/api/oauth2/authorize`. If the user isn't logged in already, and
#  auto_login is not set, the user will be dumped on the hub's home page, without
#  any context on what to do next.
#  
#  Setting this to true will automatically redirect users to login if they aren't
#  logged in *only* on the `/hub/api/oauth2/authorize` endpoint.
#  
#  .. versionadded:: 1.5
#  Default: False
# c.Authenticator.auto_login_oauth2_authorize = False

## Set of usernames that are not allowed to log in.
#  
#  Use this with supported authenticators to restrict which users can not log in.
#  This is an additional block list that further restricts users, beyond whatever
#  restrictions the authenticator has in place.
#  
#  If empty, does not perform any additional restriction.
#  
#  .. versionadded: 0.9
#  
#  .. versionchanged:: 5.2
#      Users blocked via `blocked_users` that may have logged in in the past
#      have all permissions and group membership revoked
#      and all servers stopped at JupyterHub startup.
#      Previously, User permissions (e.g. API tokens)
#      and servers were unaffected and required additional
#      administrator operations to block after a user is added to `blocked_users`.
#  
#  .. versionchanged:: 1.2
#      `Authenticator.blacklist` renamed to `blocked_users`
#  Default: set()
# c.Authenticator.blocked_users = set()

## Delete any users from the database that do not pass validation
#  
#          When JupyterHub starts, `.add_user` will be called
#          on each user in the database to verify that all users are still valid.
#  
#          If `delete_invalid_users` is True,
#          any users that do not pass validation will be deleted from the database.
#          Use this if users might be deleted from an external system,
#          such as local user accounts.
#  
#          If False (default), invalid users remain in the Hub's database
#          and a warning will be issued.
#          This is the default to avoid data loss due to config changes.
#  Default: False
# c.Authenticator.delete_invalid_users = False

## Enable persisting auth_state (if available).
#  
#          auth_state will be encrypted and stored in the Hub's database.
#          This can include things like authentication tokens, etc.
#          to be passed to Spawners as environment variables.
#  
#          Encrypting auth_state requires the cryptography package.
#  
#          Additionally, the JUPYTERHUB_CRYPT_KEY environment variable must
#          contain one (or more, separated by ;) 32B encryption keys.
#          These can be either base64 or hex-encoded.
#  
#          If encryption is unavailable, auth_state cannot be persisted.
#  
#          New in JupyterHub 0.8
#  Default: False
# c.Authenticator.enable_auth_state = False

## Let authenticator manage user groups
#  
#          If True, Authenticator.authenticate and/or .refresh_user
#          may return a list of group names in the 'groups' field,
#          which will be assigned to the user.
#  
#          All group-assignment APIs are disabled if this is True.
#  Default: False
# c.Authenticator.manage_groups = False

## Let authenticator manage roles
#  
#          If True, Authenticator.authenticate and/or .refresh_user
#          may return a list of roles in the 'roles' field,
#          which will be added to the database.
#  
#          When enabled, all role management will be handled by the
#          authenticator; in particular, assignment of roles via
#          `JupyterHub.load_roles` traitlet will not be possible.
#  
#          .. versionadded:: 5.0
#  Default: False
# c.Authenticator.manage_roles = False

## The prompt string for the extra OTP (One Time Password) field.
#  
#  .. versionadded:: 5.0
#  Default: 'OTP:'
# c.Authenticator.otp_prompt = 'OTP:'

## An optional hook function that you can implement to do some bootstrapping work
#  during authentication. For example, loading user account details from an
#  external system.
#  
#  This function is called after the user has passed all authentication checks
#  and is ready to successfully authenticate. This function must return the
#  auth_model dict reguardless of changes to it. The hook is called with 3
#  positional arguments: `(authenticator, handler, auth_model)`.
#  
#  This may be a coroutine.
#  
#  .. versionadded: 1.0
#  
#  Example::
#  
#      import os
#      import pwd
#      def my_hook(authenticator, handler, auth_model):
#          user_data = pwd.getpwnam(auth_model['name'])
#          spawn_data = {
#              'pw_data': user_data
#              'gid_list': os.getgrouplist(auth_model['name'], user_data.pw_gid)
#          }
#  
#          if auth_model['auth_state'] is None:
#              auth_model['auth_state'] = {}
#          auth_model['auth_state']['spawn_data'] = spawn_data
#  
#          return auth_model
#  
#      c.Authenticator.post_auth_hook = my_hook
#  Default: None
# c.Authenticator.post_auth_hook = None

## Force refresh of auth prior to spawn.
#  
#          This forces :meth:`.refresh_user` to be called prior to launching
#          a server, to ensure that auth state is up-to-date.
#  
#          This can be important when e.g. auth tokens that may have expired
#          are passed to the spawner via environment variables from auth_state.
#  
#          If refresh_user cannot refresh the user auth data,
#          launch will fail until the user logs in again.
#  Default: False
# c.Authenticator.refresh_pre_spawn = False

## Prompt for OTP (One Time Password) in the login form.
#  
#  .. versionadded:: 5.0
#  Default: False
# c.Authenticator.request_otp = False

## Reset managed roles to result of `load_managed_roles()` on startup.
#  
#          If True:
#            - stale managed roles will be removed,
#            - stale assignments to managed roles will be removed.
#  
#          Any role not present in `load_managed_roles()` will be considered
#  'stale'.
#  
#          The 'stale' status for role assignments is also determined from
#  `load_managed_roles()` result:
#  
#          - user role assignments status will depend on whether the `users` key
#  is defined or not:
#  
#            * if a list is defined under the `users` key and the user is not listed, then the user role assignment will be considered 'stale',
#            * if the `users` key is not provided, the user role assignment will be preserved;
#          - service and group role assignments will be considered 'stale':
#  
#            * if not included in the `services` and `groups` list,
#            * if the `services` and `groups` keys are not provided.
#  
#          .. versionadded:: 5.0
#  Default: False
# c.Authenticator.reset_managed_roles_on_startup = False

## Dictionary mapping authenticator usernames to JupyterHub users.
#  
#          Primarily used to normalize OAuth user names to local users.
#  Default: {}
# c.Authenticator.username_map = {}

## Regular expression pattern that all valid usernames must match.
#  
#  If a username does not match the pattern specified here, authentication will
#  not be attempted.
#  
#  If not set, allow any username.
#  Default: ''
# c.Authenticator.username_pattern = ''

## Deprecated, use `Authenticator.allowed_users`
#  Default: set()
# c.Authenticator.whitelist = set()

#------------------------------------------------------------------------------
# NullAuthenticator(Authenticator) configuration
#------------------------------------------------------------------------------
## Null Authenticator for JupyterHub
#  
#      For cases where authentication should be disabled,
#      e.g. only allowing access via API tokens.
#  
#      .. versionadded:: 2.0

## 
#  See also: Authenticator.admin_users
# c.NullAuthenticator.admin_users = set()

## 
#  See also: Authenticator.allow_all
# c.NullAuthenticator.allow_all = False

## 
#  See also: Authenticator.allow_existing_users
# c.NullAuthenticator.allow_existing_users = False

## 
#  See also: Authenticator.allowed_users
# c.NullAuthenticator.allowed_users = set()

## Is there any allow config?
#  See also: Authenticator.any_allow_config
# c.NullAuthenticator.any_allow_config = False

## The max age (in seconds) of authentication info
#  See also: Authenticator.auth_refresh_age
# c.NullAuthenticator.auth_refresh_age = 300

## 
#  See also: Authenticator.auto_login_oauth2_authorize
# c.NullAuthenticator.auto_login_oauth2_authorize = False

## 
#  See also: Authenticator.blocked_users
# c.NullAuthenticator.blocked_users = set()

## Delete any users from the database that do not pass validation
#  See also: Authenticator.delete_invalid_users
# c.NullAuthenticator.delete_invalid_users = False

## Enable persisting auth_state (if available).
#  See also: Authenticator.enable_auth_state
# c.NullAuthenticator.enable_auth_state = False

## Let authenticator manage user groups
#  See also: Authenticator.manage_groups
# c.NullAuthenticator.manage_groups = False

## Let authenticator manage roles
#  See also: Authenticator.manage_roles
# c.NullAuthenticator.manage_roles = False

## 
#  See also: Authenticator.otp_prompt
# c.NullAuthenticator.otp_prompt = 'OTP:'

## 
#  See also: Authenticator.post_auth_hook
# c.NullAuthenticator.post_auth_hook = None

## Force refresh of auth prior to spawn.
#  See also: Authenticator.refresh_pre_spawn
# c.NullAuthenticator.refresh_pre_spawn = False

## 
#  See also: Authenticator.request_otp
# c.NullAuthenticator.request_otp = False

## Reset managed roles to result of `load_managed_roles()` on startup.
#  See also: Authenticator.reset_managed_roles_on_startup
# c.NullAuthenticator.reset_managed_roles_on_startup = False

## Dictionary mapping authenticator usernames to JupyterHub users.
#  See also: Authenticator.username_map
# c.NullAuthenticator.username_map = {}

## 
#  See also: Authenticator.username_pattern
# c.NullAuthenticator.username_pattern = ''

## Deprecated, use `Authenticator.allowed_users`
#  See also: Authenticator.whitelist
# c.NullAuthenticator.whitelist = set()

#------------------------------------------------------------------------------
# Proxy(LoggingConfigurable) configuration
#------------------------------------------------------------------------------
## Base class for configurable proxies that JupyterHub can use.
#  
#      A proxy implementation should subclass this and must define the following
#  methods:
#  
#      - :meth:`.get_all_routes` return a dictionary of all JupyterHub-related routes
#      - :meth:`.add_route` adds a route
#      - :meth:`.delete_route` deletes a route
#  
#      In addition to these, the following method(s) may need to be implemented:
#  
#      - :meth:`.start` start the proxy, if it should be launched by the Hub
#        instead of externally managed.
#        If the proxy is externally managed, it should set :attr:`should_start` to False.
#      - :meth:`.stop` stop the proxy. Only used if :meth:`.start` is also used.
#  
#      And the following method(s) are optional, but can be provided:
#  
#      - :meth:`.get_route` gets a single route.
#        There is a default implementation that extracts data from :meth:`.get_all_routes`,
#        but implementations may choose to provide a more efficient implementation
#        of fetching a single route.

## Additional routes to be maintained in the proxy.
#  
#  A dictionary with a route specification as key, and a URL as target. The hub
#  will ensure this route is present in the proxy.
#  
#  If the hub is running in host based mode (with JupyterHub.subdomain_host set),
#  the routespec *must* have a domain component (example.com/my-url/). If the hub
#  is not running in host based mode, the routespec *must not* have a domain
#  component (/my-url/).
#  
#  Helpful when the hub is running in API-only mode.
#  Default: {}
# c.Proxy.extra_routes = {}

## Should the Hub start the proxy
#  
#          If True, the Hub will start the proxy and stop it.
#          Set to False if the proxy is managed externally,
#          such as by systemd, docker, or another service manager.
#  Default: True
# c.Proxy.should_start = True

#------------------------------------------------------------------------------
# ConfigurableHTTPProxy(Proxy) configuration
#------------------------------------------------------------------------------
## Proxy implementation for the default configurable-http-proxy.
#  
#      This is the default proxy implementation
#      for running the nodejs proxy `configurable-http-proxy`.
#  
#      If the proxy should not be run as a subprocess of the Hub,
#      (e.g. in a separate container),
#      set::
#  
#          c.ConfigurableHTTPProxy.should_start = False

## The ip (or hostname) of the proxy's API endpoint
#  Default: ''
# c.ConfigurableHTTPProxy.api_url = ''

## The Proxy auth token
#  
#          Loaded from the CONFIGPROXY_AUTH_TOKEN env variable by default.
#  Default: ''
# c.ConfigurableHTTPProxy.auth_token = ''

## Interval (in seconds) at which to check if the proxy is running.
#  Default: 5
# c.ConfigurableHTTPProxy.check_running_interval = 5

## The command to start the proxy
#  Default: ['configurable-http-proxy']
# c.ConfigurableHTTPProxy.command = ['configurable-http-proxy']

## The number of requests allowed to be concurrently outstanding to the proxy
#  
#  Limiting this number avoids potential timeout errors by sending too many
#  requests to update the proxy at once
#  Default: 10
# c.ConfigurableHTTPProxy.concurrency = 10

## Add debug-level logging to the Proxy.
#  Default: False
# c.ConfigurableHTTPProxy.debug = False

## 
#  See also: Proxy.extra_routes
# c.ConfigurableHTTPProxy.extra_routes = {}

## Proxy log level
#  Choices: any of ['debug', 'info', 'warn', 'error'] (case-insensitive)
#  Default: 'info'
# c.ConfigurableHTTPProxy.log_level = 'info'

## File in which to write the PID of the proxy process.
#  Default: 'jupyterhub-proxy.pid'
# c.ConfigurableHTTPProxy.pid_file = 'jupyterhub-proxy.pid'

## Should the Hub start the proxy
#  See also: Proxy.should_start
# c.ConfigurableHTTPProxy.should_start = True

#------------------------------------------------------------------------------
# Spawner(LoggingConfigurable) configuration
#------------------------------------------------------------------------------
## Base class for spawning single-user notebook servers.
#  
#      Subclass this, and override the following methods:
#  
#      - load_state
#      - get_state
#      - start
#      - stop
#      - poll
#  
#      As JupyterHub supports multiple users, an instance of the Spawner subclass
#      is created for each user. If there are 20 JupyterHub users, there will be 20
#      instances of the subclass.

## Hook to apply inputs from user_options to the Spawner.
#  
#  Typically takes values in user_options, validates them, and updates Spawner
#  attributes::
#  
#      def apply_user_options(spawner, user_options):
#          if "image" in user_options and isinstance(user_options["image"], str):
#              spawner.image = user_options["image"]
#  
#      c.Spawner.apply_user_options = apply_user_options
#  
#  `apply_user_options` *may* be async.
#  
#  Default: do nothing.
#  
#  Typically a callable which takes `(spawner: Spawner, user_options: dict)`, but
#  for simple cases this can be a dict mapping user option fields to Spawner
#  attribute names, e.g.::
#  
#      c.Spawner.apply_user_options = {"image_input": "image"}
#      c.Spawner.options_from_form = "simple"
#  
#  allows users to specify the image attribute, but not any others. Because
#  `user_options` generally comes in as strings in form data, the dictionary mode
#  uses traitlets `from_string` to coerce strings to values, which allows setting
#  simple values from strings (e.g. numbers) without needing to implement
#  callable hooks.
#  
#  .. note::
#  
#      Because `user_options` is user input
#      and may be set directly via the REST API,
#      no assumptions should be made on its structure or contents.
#      An empty dict should always be supported.
#      Make sure to validate any inputs before applying them,
#      either in this callable, or in whatever is consuming the value
#      if this is a dict.
#  
#  .. versionadded:: 5.3
#  
#      Prior to 5.3, applying user options must be done in `Spawner.start()`
#      or `Spawner.pre_spawn_hook()`.
#  Default: None
# c.Spawner.apply_user_options = None

## Extra arguments to be passed to the single-user server.
#  
#  Some spawners allow shell-style expansion here, allowing you to use
#  environment variables here. Most, including the default, do not. Consult the
#  documentation for your spawner to verify!
#  Default: []
# c.Spawner.args = []

## An optional hook function that you can implement to pass `auth_state` to the
#  spawner after it has been initialized but before it starts. The `auth_state`
#  dictionary may be set by the `.authenticate()` method of the authenticator.
#  This hook enables you to pass some or all of that information to your spawner.
#  
#  Example::
#  
#      def userdata_hook(spawner, auth_state):
#          spawner.userdata = auth_state["userdata"]
#  
#      c.Spawner.auth_state_hook = userdata_hook
#  Default: None
# c.Spawner.auth_state_hook = None

## The command used for starting the single-user server.
#  
#  Provide either a string or a list containing the path to the startup script
#  command. Extra arguments, other than this path, should be provided via `args`.
#  
#  This is usually set if you want to start the single-user server in a different
#  python environment (with virtualenv/conda) than JupyterHub itself.
#  
#  Some spawners allow shell-style expansion here, allowing you to use
#  environment variables. Most, including the default, do not. Consult the
#  documentation for your spawner to verify!
#  Default: ['jupyterhub-singleuser']
# c.Spawner.cmd = ['jupyterhub-singleuser']

## Maximum number of consecutive failures to allow before shutting down
#  JupyterHub.
#  
#  This helps JupyterHub recover from a certain class of problem preventing
#  launch in contexts where the Hub is automatically restarted (e.g. systemd,
#  docker, kubernetes).
#  
#  A limit of 0 means no limit and consecutive failures will not be tracked.
#  Default: 0
# c.Spawner.consecutive_failure_limit = 0

## Minimum number of cpu-cores a single-user notebook server is guaranteed to
#  have available.
#  
#  If this value is set to 0.5, allows use of 50% of one CPU. If this value is
#  set to 2, allows use of up to 2 CPUs.
#  
#  **This is a configuration setting. Your spawner must implement support for the
#  limit to work.** The default spawner, `LocalProcessSpawner`, does **not**
#  implement this support. A custom spawner **must** add support for this setting
#  for it to be enforced.
#  Default: None
# c.Spawner.cpu_guarantee = None

## Maximum number of cpu-cores a single-user notebook server is allowed to use.
#  
#  If this value is set to 0.5, allows use of 50% of one CPU. If this value is
#  set to 2, allows use of up to 2 CPUs.
#  
#  The single-user notebook server will never be scheduled by the kernel to use
#  more cpu-cores than this. There is no guarantee that it can access this many
#  cpu-cores.
#  
#  **This is a configuration setting. Your spawner must implement support for the
#  limit to work.** The default spawner, `LocalProcessSpawner`, does **not**
#  implement this support. A custom spawner **must** add support for this setting
#  for it to be enforced.
#  Default: None
# c.Spawner.cpu_limit = None

## Enable debug-logging of the single-user server
#  Default: False
# c.Spawner.debug = False

## The URL the single-user server should start in.
#  
#  `{username}` will be expanded to the user's username
#  
#  Example uses:
#  
#  - You can set `notebook_dir` to `/` and `default_url` to `/tree/home/{username}` to allow people to
#    navigate the whole filesystem from their notebook server, but still start in their home directory.
#  - Start with `/notebooks` instead of `/tree` if `default_url` points to a notebook instead of a directory.
#  - You can set this to `/lab` to have JupyterLab start by default, rather than Jupyter Notebook.
#  Default: ''
# c.Spawner.default_url = ''

## Disable per-user configuration of single-user servers.
#  
#  When starting the user's single-user server, any config file found in the
#  user's $HOME directory will be ignored.
#  
#  Note: a user could circumvent this if the user modifies their Python
#  environment, such as when they have their own conda environments / virtualenvs
#  / containers.
#  Default: False
# c.Spawner.disable_user_config = False

## List of environment variables for the single-user server to inherit from the
#  JupyterHub process.
#  
#  This list is used to ensure that sensitive information in the JupyterHub
#  process's environment (such as `CONFIGPROXY_AUTH_TOKEN`) is not passed to the
#  single-user server's process.
#  Default: ['JUPYTERHUB_SINGLEUSER_APP']
# c.Spawner.env_keep = ['JUPYTERHUB_SINGLEUSER_APP']

## Extra environment variables to set for the single-user server's process.
#  
#  Environment variables that end up in the single-user server's process come from 3 sources:
#    - This `environment` configurable
#    - The JupyterHub process' environment variables that are listed in `env_keep`
#    - Variables to establish contact between the single-user notebook and the hub (such as JUPYTERHUB_API_TOKEN)
#  
#  The `environment` configurable should be set by JupyterHub administrators to
#  add installation specific environment variables. It is a dict where the key is
#  the name of the environment variable, and the value can be a string or a
#  callable. If it is a callable, it will be called with one parameter (the
#  spawner instance), and should return a string fairly quickly (no blocking
#  operations please!).
#  
#  Note that the spawner class' interface is not guaranteed to be exactly same
#  across upgrades, so if you are using the callable take care to verify it
#  continues to work after upgrades!
#  
#  .. versionchanged:: 1.2
#      environment from this configuration has highest priority,
#      allowing override of 'default' env variables,
#      such as JUPYTERHUB_API_URL.
#  Default: {}
# c.Spawner.environment = {}

## Override specific traitlets based on group membership of the user.
#  
#  This can be a dict, or a callable that returns a dict. The keys of the dict
#  are *only* used for lexicographical sorting, to guarantee consistent ordering
#  of the overrides. If it is a callable, it may be async, and will be passed one
#  parameter - the spawner instance. It should return a dictionary.
#  
#  The values of the dict are dicts with the following keys:
#  
#  - `"groups"` - If the user belongs to *any* of these groups, these overrides are
#    applied to their server before spawning.
#  - `"spawner_override"` - a dictionary with overrides to apply to the Spawner
#    settings. Each value can be either the final value to change or a callable that
#    take the `Spawner` instance as parameter and returns the final value.
#    If the traitlet being overriden is a *dictionary*, the dictionary
#    will be *recursively updated*, rather than overriden. If you want to
#    remove a key, set its value to `None`.
#  
#  Example:
#  
#      The following example config will:
#  
#      1. Add the environment variable "AM_I_GROUP_ALPHA" to everyone in the "group-alpha" group
#      2. Add the environment variable "AM_I_GROUP_BETA" to everyone in the "group-beta" group.
#         If a user is part of both "group-beta" and "group-alpha", they will get *both* these env
#         vars, due to the dictionary merging functionality.
#      3. Add a higher memory limit for everyone in the "group-beta" group.
#  
#      ::
#  
#          c.Spawner.group_overrides = {
#              "01-group-alpha-env-add": {
#                  "groups": ["group-alpha"],
#                  "spawner_override": {"environment": {"AM_I_GROUP_ALPHA": "yes"}},
#              },
#              "02-group-beta-env-add": {
#                  "groups": ["group-beta"],
#                  "spawner_override": {"environment": {"AM_I_GROUP_BETA": "yes"}},
#              },
#              "03-group-beta-mem-limit": {
#                  "groups": ["group-beta"],
#                  "spawner_override": {"mem_limit": "2G"}
#              }
#          }
#  Default: traitlets.Undefined
# c.Spawner.group_overrides = traitlets.Undefined

## Timeout (in seconds) before giving up on a spawned HTTP server
#  
#  Once a server has successfully been spawned, this is the amount of time we
#  wait before assuming that the server is unable to accept connections.
#  Default: 30
# c.Spawner.http_timeout = 30

## The URL the single-user server should connect to the Hub.
#  
#  If the Hub URL set in your JupyterHub config is not reachable from spawned
#  notebooks, you can set differnt URL by this config.
#  
#  Is None if you don't need to change the URL.
#  Default: None
# c.Spawner.hub_connect_url = None

## The IP address (or hostname) the single-user server should listen on.
#  
#  Usually either '127.0.0.1' (default) or '0.0.0.0'. On IPv6 only networks use
#  '::1' or '::'.
#  
#  If the spawned singleuser server is running JupyterHub 5.3.0 later You can set
#  this to the empty string '' to indicate both IPv4 and IPv6.
#  
#  The JupyterHub proxy implementation should be able to send packets to this
#  interface.
#  
#  Subclasses which launch remotely or in containers should override the default
#  to '0.0.0.0'.
#  
#  .. versionchanged:: 5.3
#      An empty string '' means all interfaces (IPv4 and IPv6). Prior to this
#      the behaviour of '' was not defined.
#  
#  .. versionchanged:: 2.0
#      Default changed to '127.0.0.1', from unspecified.
#  Default: '127.0.0.1'
# c.Spawner.ip = '127.0.0.1'

## Minimum number of bytes a single-user notebook server is guaranteed to have
#  available.
#  
#  Allows the following suffixes:
#    - K -> Kilobytes
#    - M -> Megabytes
#    - G -> Gigabytes
#    - T -> Terabytes
#  
#  **This is a configuration setting. Your spawner must implement support for the
#  limit to work.** The default spawner, `LocalProcessSpawner`, does **not**
#  implement this support. A custom spawner **must** add support for this setting
#  for it to be enforced.
#  Default: None
# c.Spawner.mem_guarantee = None

## Maximum number of bytes a single-user notebook server is allowed to use.
#  
#  Allows the following suffixes:
#    - K -> Kilobytes
#    - M -> Megabytes
#    - G -> Gigabytes
#    - T -> Terabytes
#  
#  If the single user server tries to allocate more memory than this, it will
#  fail. There is no guarantee that the single-user notebook server will be able
#  to allocate this much memory - only that it can not allocate more than this.
#  
#  **This is a configuration setting. Your spawner must implement support for the
#  limit to work.** The default spawner, `LocalProcessSpawner`, does **not**
#  implement this support. A custom spawner **must** add support for this setting
#  for it to be enforced.
#  Default: None
# c.Spawner.mem_limit = None

## Path to the notebook directory for the single-user server.
#  
#  The user sees a file listing of this directory when the notebook interface is
#  started. The current interface does not easily allow browsing beyond the
#  subdirectories in this directory's tree.
#  
#  `~` will be expanded to the home directory of the user, and {username} will be
#  replaced with the name of the user.
#  
#  Note that this does *not* prevent users from accessing files outside of this
#  path! They can do so with many other means.
#  Default: ''
# c.Spawner.notebook_dir = ''

## Allowed scopes for oauth tokens issued by this server's oauth client.
#  
#          This sets the maximum and default scopes
#          assigned to oauth tokens issued by a single-user server's
#          oauth client (i.e. tokens stored in browsers after authenticating with the server),
#          defining what actions the server can take on behalf of logged-in users.
#  
#          Access to the current server will always be included in this list.
#          This property contains additional scopes.
#          Default is an empty list, meaning minimal permissions to identify users,
#          no actions can be taken on their behalf.
#  
#          If callable, will be called with the Spawner as a single argument.
#          Callables may be async.
#  Default: traitlets.Undefined
# c.Spawner.oauth_client_allowed_scopes = traitlets.Undefined

## Allowed roles for oauth tokens.
#  
#          Deprecated in 3.0: use oauth_client_allowed_scopes
#  Default: traitlets.Undefined
# c.Spawner.oauth_roles = traitlets.Undefined

## An HTML form for options a user can specify on launching their server.
#  
#  The surrounding `<form>` element and the submit button are already provided.
#  
#  For example:
#  
#  .. code:: html
#  
#      Set your key:
#      <input name="key" val="default_key"></input>
#      <br>
#      Choose a letter:
#      <select name="letter" multiple="true">
#        <option value="A">The letter A</option>
#        <option value="B">The letter B</option>
#      </select>
#  
#  The data from this form submission will be passed on to your spawner in
#  `self.user_options`
#  
#  Instead of a form snippet string, this could also be a callable that takes as
#  one parameter the current spawner instance and returns a string. The callable
#  will be called asynchronously if it returns a future, rather than a str. Note
#  that the interface of the spawner class is not deemed stable across versions,
#  so using this functionality might cause your JupyterHub upgrades to break.
#  Default: traitlets.Undefined
# c.Spawner.options_form = traitlets.Undefined

## Interpret HTTP form data
#  
#  Form data will always arrive as a dict of lists of strings. Override this
#  function to understand single-values, numbers, etc.
#  
#  This should coerce form data into the structure expected by self.user_options,
#  which must be a dict, and should be JSON-serializeable, though it can contain
#  bytes in addition to standard JSON data types.
#  
#  This method should not have any side effects. Any handling of `user_options`
#  should be done in `.apply_user_options()` (JupyterHub 5.3) or `.start()`
#  (JupyterHub 5.2 or older) to ensure consistent behavior across servers spawned
#  via the API and form submission page.
#  
#  Instances will receive this data on self.user_options, after passing through
#  this function, prior to `Spawner.start`.
#  
#  .. versionchanged:: 1.0
#      user_options are persisted in the JupyterHub database to be reused
#      on subsequent spawns if no options are given.
#      user_options is serialized to JSON as part of this persistence
#      (with additional support for bytes in case of uploaded file data),
#      and any non-bytes non-jsonable values will be replaced with None
#      if the user_options are re-used.
#  
#  .. versionadded:: 5.3
#      The strings `'simple'` and `'passthrough'` may be specified to select some predefined behavior.
#      These are the only string values accepted.
#  
#      `'passthrough'` is the longstanding default behavior,
#      where form data is stored in `user_options` without modification.
#      With `'passthrough'`, `user_options` from a form will always be a dict of lists of strings.
#  
#      `'simple'` applies some minimal processing that works for most simple
#  forms:
#  
#      - Single-value fields get unpacked from lists.
#        They are still always strings, no attempt is made to parse numbers, etc..
#      - Multi-value fields are left alone.
#      - The default checked value of "on" for a checkbox is converted to True.
#        This is the only non-string value that can be produced.
#  
#      Example for `'simple'`::
#  
#          {
#              "image": ["myimage"],
#              "checked": ["on"], # checkbox
#              "multi-select": ["a", "b"],
#          }
#          # becomes
#          {
#              "image": "myimage",
#              "checked": True,
#              "multi-select": ["a", "b"],
#          }
#  Default: traitlets.Undefined
# c.Spawner.options_from_form = traitlets.Undefined

## Interval (in seconds) on which to poll the spawner for single-user server's
#  status.
#  
#  At every poll interval, each spawner's `.poll` method is called, which checks
#  if the single-user server is still running. If it isn't running, then
#  JupyterHub modifies its own state accordingly and removes appropriate routes
#  from the configurable proxy.
#  Default: 30
# c.Spawner.poll_interval = 30

## Jitter fraction for poll_interval.
#  
#  Avoids alignment of poll calls for many Spawners, e.g. when restarting
#  JupyterHub, which restarts all polls for running Spawners.
#  
#  `poll_jitter=0` means no jitter, 0.1 means 10%, etc.
#  Default: 0.1
# c.Spawner.poll_jitter = 0.1

## The port for single-user servers to listen on.
#  
#  Defaults to `0`, which uses a randomly allocated port number each time.
#  
#  If set to a non-zero value, all Spawners will use the same port, which only
#  makes sense if each server is on a different address, e.g. in containers.
#  
#  New in version 0.7.
#  Default: 0
# c.Spawner.port = 0

## An optional hook function that you can implement to do work after the spawner
#  stops.
#  
#  This can be set independent of any concrete spawner implementation.
#  Default: None
# c.Spawner.post_stop_hook = None

## An optional hook function that you can implement to do some bootstrapping work
#  before the spawner starts. For example, create a directory for your user or
#  load initial content.
#  
#  This can be set independent of any concrete spawner implementation.
#  
#  This maybe a coroutine.
#  
#  Example::
#  
#      def my_hook(spawner):
#          username = spawner.user.name
#          spawner.environment["GREETING"] = f"Hello {username}"
#  
#      c.Spawner.pre_spawn_hook = my_hook
#  Default: None
# c.Spawner.pre_spawn_hook = None

## An optional hook function that you can implement to modify the ready event,
#  which will be shown to the user on the spawn progress page when their server
#  is ready.
#  
#  This can be set independent of any concrete spawner implementation.
#  
#  This maybe a coroutine.
#  
#  Example::
#  
#      async def my_ready_hook(spawner, ready_event):
#          ready_event["html_message"] = f"Server {spawner.name} is ready for {spawner.user.name}"
#          return ready_event
#  
#      c.Spawner.progress_ready_hook = my_ready_hook
#  Default: None
# c.Spawner.progress_ready_hook = None

## The list of scopes to request for $JUPYTERHUB_API_TOKEN
#  
#          If not specified, the scopes in the `server` role will be used
#          (unchanged from pre-4.0).
#  
#          If callable, will be called with the Spawner instance as its sole argument
#          (JupyterHub user available as spawner.user).
#  
#          JUPYTERHUB_API_TOKEN will be assigned the _subset_ of these scopes
#          that are held by the user (as in oauth_client_allowed_scopes).
#  
#          .. versionadded:: 4.0
#  Default: traitlets.Undefined
# c.Spawner.server_token_scopes = traitlets.Undefined

## List of SSL alt names
#  
#          May be set in config if all spawners should have the same value(s),
#          or set at runtime by Spawner that know their names.
#  Default: []
# c.Spawner.ssl_alt_names = []

## Whether to include `DNS:localhost`, `IP:127.0.0.1` in alt names
#  Default: True
# c.Spawner.ssl_alt_names_include_local = True

## Timeout (in seconds) before giving up on starting of single-user server.
#  
#  This is the timeout for start to return, not the timeout for the server to
#  respond. Callers of spawner.start will assume that startup has failed if it
#  takes longer than this. start should return when the server process is started
#  and its location is known.
#  Default: 60
# c.Spawner.start_timeout = 60

#------------------------------------------------------------------------------
# LocalProcessSpawner(Spawner) configuration
#------------------------------------------------------------------------------
## A Spawner that uses `subprocess.Popen` to start single-user servers as local
#  processes.
#  
#  Requires local UNIX users matching the authenticated users to exist. Does not
#  work on Windows.
#  
#  This is the default spawner for JupyterHub.
#  
#  Note: This spawner does not implement CPU / memory guarantees and limits.

## 
#  See also: Spawner.apply_user_options
# c.LocalProcessSpawner.apply_user_options = None

## 
#  See also: Spawner.args
# c.LocalProcessSpawner.args = []

## 
#  See also: Spawner.auth_state_hook
# c.LocalProcessSpawner.auth_state_hook = None

## 
#  See also: Spawner.cmd
# c.LocalProcessSpawner.cmd = ['jupyterhub-singleuser']

## 
#  See also: Spawner.consecutive_failure_limit
# c.LocalProcessSpawner.consecutive_failure_limit = 0

## 
#  See also: Spawner.cpu_guarantee
# c.LocalProcessSpawner.cpu_guarantee = None

## 
#  See also: Spawner.cpu_limit
# c.LocalProcessSpawner.cpu_limit = None

## Enable debug-logging of the single-user server
#  See also: Spawner.debug
# c.LocalProcessSpawner.debug = False

## 
#  See also: Spawner.default_url
# c.LocalProcessSpawner.default_url = ''

## 
#  See also: Spawner.disable_user_config
# c.LocalProcessSpawner.disable_user_config = False

## 
#  See also: Spawner.env_keep
# c.LocalProcessSpawner.env_keep = ['JUPYTERHUB_SINGLEUSER_APP']

## 
#  See also: Spawner.environment
# c.LocalProcessSpawner.environment = {}

## 
#  See also: Spawner.group_overrides
# c.LocalProcessSpawner.group_overrides = traitlets.Undefined

## 
#  See also: Spawner.http_timeout
# c.LocalProcessSpawner.http_timeout = 30

## 
#  See also: Spawner.hub_connect_url
# c.LocalProcessSpawner.hub_connect_url = None

## Seconds to wait for single-user server process to halt after SIGINT.
#  
#  If the process has not exited cleanly after this many seconds, a SIGTERM is
#  sent.
#  Default: 10
# c.LocalProcessSpawner.interrupt_timeout = 10

## 
#  See also: Spawner.ip
# c.LocalProcessSpawner.ip = '127.0.0.1'

## Seconds to wait for process to halt after SIGKILL before giving up.
#  
#  If the process does not exit cleanly after this many seconds of SIGKILL, it
#  becomes a zombie process. The hub process will log a warning and then give up.
#  Default: 5
# c.LocalProcessSpawner.kill_timeout = 5

## 
#  See also: Spawner.mem_guarantee
# c.LocalProcessSpawner.mem_guarantee = None

## 
#  See also: Spawner.mem_limit
# c.LocalProcessSpawner.mem_limit = None

## 
#  See also: Spawner.notebook_dir
# c.LocalProcessSpawner.notebook_dir = ''

## Allowed scopes for oauth tokens issued by this server's oauth client.
#  See also: Spawner.oauth_client_allowed_scopes
# c.LocalProcessSpawner.oauth_client_allowed_scopes = traitlets.Undefined

## Allowed roles for oauth tokens.
#  See also: Spawner.oauth_roles
# c.LocalProcessSpawner.oauth_roles = traitlets.Undefined

## 
#  See also: Spawner.options_form
# c.LocalProcessSpawner.options_form = traitlets.Undefined

## 
#  See also: Spawner.options_from_form
# c.LocalProcessSpawner.options_from_form = traitlets.Undefined

## 
#  See also: Spawner.poll_interval
# c.LocalProcessSpawner.poll_interval = 30

## 
#  See also: Spawner.poll_jitter
# c.LocalProcessSpawner.poll_jitter = 0.1

## Extra keyword arguments to pass to Popen
#  
#          when spawning single-user servers.
#  
#          For example::
#  
#              popen_kwargs = dict(shell=True)
#  Default: {}
# c.LocalProcessSpawner.popen_kwargs = {}

## 
#  See also: Spawner.port
# c.LocalProcessSpawner.port = 0

## 
#  See also: Spawner.post_stop_hook
# c.LocalProcessSpawner.post_stop_hook = None

## 
#  See also: Spawner.pre_spawn_hook
# c.LocalProcessSpawner.pre_spawn_hook = None

## 
#  See also: Spawner.progress_ready_hook
# c.LocalProcessSpawner.progress_ready_hook = None

## The list of scopes to request for $JUPYTERHUB_API_TOKEN
#  See also: Spawner.server_token_scopes
# c.LocalProcessSpawner.server_token_scopes = traitlets.Undefined

## Specify a shell command to launch.
#  
#          The single-user command will be appended to this list,
#          so it sould end with `-c` (for bash) or equivalent.
#  
#          For example::
#  
#              c.LocalProcessSpawner.shell_cmd = ['bash', '-l', '-c']
#  
#          to launch with a bash login shell, which would set up the user's own
#  complete environment.
#  
#          .. warning::
#  
#              Using shell_cmd gives users control over PATH, etc.,
#              which could change what the jupyterhub-singleuser launch command does.
#              Only use this for trusted users.
#  Default: []
# c.LocalProcessSpawner.shell_cmd = []

## List of SSL alt names
#  See also: Spawner.ssl_alt_names
# c.LocalProcessSpawner.ssl_alt_names = []

## Whether to include `DNS:localhost`, `IP:127.0.0.1` in alt names
#  See also: Spawner.ssl_alt_names_include_local
# c.LocalProcessSpawner.ssl_alt_names_include_local = True

## 
#  See also: Spawner.start_timeout
# c.LocalProcessSpawner.start_timeout = 60

## Seconds to wait for single-user server process to halt after SIGTERM.
#  
#  If the process does not exit cleanly after this many seconds of SIGTERM, a
#  SIGKILL is sent.
#  Default: 5
# c.LocalProcessSpawner.term_timeout = 5

#------------------------------------------------------------------------------
# SimpleLocalProcessSpawner(LocalProcessSpawner) configuration
#------------------------------------------------------------------------------
## A version of LocalProcessSpawner that doesn't require users to exist on the
#  system beforehand.
#  
#  Only use this for testing.
#  
#  Note: DO NOT USE THIS FOR PRODUCTION USE CASES! It is very insecure, and
#  provides absolutely no isolation between different users!

## 
#  See also: Spawner.apply_user_options
# c.SimpleLocalProcessSpawner.apply_user_options = None

## 
#  See also: Spawner.args
# c.SimpleLocalProcessSpawner.args = []

## 
#  See also: Spawner.auth_state_hook
# c.SimpleLocalProcessSpawner.auth_state_hook = None

## 
#  See also: Spawner.cmd
# c.SimpleLocalProcessSpawner.cmd = ['jupyterhub-singleuser']

## 
#  See also: Spawner.consecutive_failure_limit
# c.SimpleLocalProcessSpawner.consecutive_failure_limit = 0

## 
#  See also: Spawner.cpu_guarantee
# c.SimpleLocalProcessSpawner.cpu_guarantee = None

## 
#  See also: Spawner.cpu_limit
# c.SimpleLocalProcessSpawner.cpu_limit = None

## Enable debug-logging of the single-user server
#  See also: Spawner.debug
# c.SimpleLocalProcessSpawner.debug = False

## 
#  See also: Spawner.default_url
# c.SimpleLocalProcessSpawner.default_url = ''

## 
#  See also: Spawner.disable_user_config
# c.SimpleLocalProcessSpawner.disable_user_config = False

## 
#  See also: Spawner.env_keep
# c.SimpleLocalProcessSpawner.env_keep = ['JUPYTERHUB_SINGLEUSER_APP']

## 
#  See also: Spawner.environment
# c.SimpleLocalProcessSpawner.environment = {}

## 
#  See also: Spawner.group_overrides
# c.SimpleLocalProcessSpawner.group_overrides = traitlets.Undefined

## Template to expand to set the user home. {username} is expanded to the
#  jupyterhub username.
#  Default: '/tmp/{username}'
# c.SimpleLocalProcessSpawner.home_dir_template = '/tmp/{username}'

## 
#  See also: Spawner.http_timeout
# c.SimpleLocalProcessSpawner.http_timeout = 30

## 
#  See also: Spawner.hub_connect_url
# c.SimpleLocalProcessSpawner.hub_connect_url = None

## 
#  See also: LocalProcessSpawner.interrupt_timeout
# c.SimpleLocalProcessSpawner.interrupt_timeout = 10

## 
#  See also: Spawner.ip
# c.SimpleLocalProcessSpawner.ip = '127.0.0.1'

## 
#  See also: LocalProcessSpawner.kill_timeout
# c.SimpleLocalProcessSpawner.kill_timeout = 5

## 
#  See also: Spawner.mem_guarantee
# c.SimpleLocalProcessSpawner.mem_guarantee = None

## 
#  See also: Spawner.mem_limit
# c.SimpleLocalProcessSpawner.mem_limit = None

## 
#  See also: Spawner.notebook_dir
# c.SimpleLocalProcessSpawner.notebook_dir = ''

## Allowed scopes for oauth tokens issued by this server's oauth client.
#  See also: Spawner.oauth_client_allowed_scopes
# c.SimpleLocalProcessSpawner.oauth_client_allowed_scopes = traitlets.Undefined

## Allowed roles for oauth tokens.
#  See also: Spawner.oauth_roles
# c.SimpleLocalProcessSpawner.oauth_roles = traitlets.Undefined

## 
#  See also: Spawner.options_form
# c.SimpleLocalProcessSpawner.options_form = traitlets.Undefined

## 
#  See also: Spawner.options_from_form
# c.SimpleLocalProcessSpawner.options_from_form = traitlets.Undefined

## 
#  See also: Spawner.poll_interval
# c.SimpleLocalProcessSpawner.poll_interval = 30

## 
#  See also: Spawner.poll_jitter
# c.SimpleLocalProcessSpawner.poll_jitter = 0.1

## Extra keyword arguments to pass to Popen
#  See also: LocalProcessSpawner.popen_kwargs
# c.SimpleLocalProcessSpawner.popen_kwargs = {}

## 
#  See also: Spawner.port
# c.SimpleLocalProcessSpawner.port = 0

## 
#  See also: Spawner.post_stop_hook
# c.SimpleLocalProcessSpawner.post_stop_hook = None

## 
#  See also: Spawner.pre_spawn_hook
# c.SimpleLocalProcessSpawner.pre_spawn_hook = None

## 
#  See also: Spawner.progress_ready_hook
# c.SimpleLocalProcessSpawner.progress_ready_hook = None

## The list of scopes to request for $JUPYTERHUB_API_TOKEN
#  See also: Spawner.server_token_scopes
# c.SimpleLocalProcessSpawner.server_token_scopes = traitlets.Undefined

## Specify a shell command to launch.
#  See also: LocalProcessSpawner.shell_cmd
# c.SimpleLocalProcessSpawner.shell_cmd = []

## List of SSL alt names
#  See also: Spawner.ssl_alt_names
# c.SimpleLocalProcessSpawner.ssl_alt_names = []

## Whether to include `DNS:localhost`, `IP:127.0.0.1` in alt names
#  See also: Spawner.ssl_alt_names_include_local
# c.SimpleLocalProcessSpawner.ssl_alt_names_include_local = True

## 
#  See also: Spawner.start_timeout
# c.SimpleLocalProcessSpawner.start_timeout = 60

## 
#  See also: LocalProcessSpawner.term_timeout
# c.SimpleLocalProcessSpawner.term_timeout = 5

#------------------------------------------------------------------------------
# DummyAuthenticator(Authenticator) configuration
#------------------------------------------------------------------------------
## Dummy Authenticator for testing
#  
#      By default, any username + password is allowed
#      If a non-empty password is set, any username will be allowed
#      if it logs in with that password.
#  
#      .. versionadded:: 1.0
#  
#      .. versionadded:: 5.0
#          `allow_all` defaults to True,
#          preserving default behavior.

## 
#  See also: Authenticator.admin_users
# c.DummyAuthenticator.admin_users = set()

## 
#  See also: Authenticator.allow_all
# c.DummyAuthenticator.allow_all = False

## 
#  See also: Authenticator.allow_existing_users
# c.DummyAuthenticator.allow_existing_users = False

## 
#  See also: Authenticator.allowed_users
# c.DummyAuthenticator.allowed_users = set()

## Is there any allow config?
#  See also: Authenticator.any_allow_config
# c.DummyAuthenticator.any_allow_config = False

## The max age (in seconds) of authentication info
#  See also: Authenticator.auth_refresh_age
# c.DummyAuthenticator.auth_refresh_age = 300

## Automatically begin the login process
#  See also: Authenticator.auto_login
# c.DummyAuthenticator.auto_login = False

## 
#  See also: Authenticator.auto_login_oauth2_authorize
# c.DummyAuthenticator.auto_login_oauth2_authorize = False

## 
#  See also: Authenticator.blocked_users
# c.DummyAuthenticator.blocked_users = set()

## Delete any users from the database that do not pass validation
#  See also: Authenticator.delete_invalid_users
# c.DummyAuthenticator.delete_invalid_users = False

## Enable persisting auth_state (if available).
#  See also: Authenticator.enable_auth_state
# c.DummyAuthenticator.enable_auth_state = False

## Let authenticator manage user groups
#  See also: Authenticator.manage_groups
# c.DummyAuthenticator.manage_groups = False

## Let authenticator manage roles
#  See also: Authenticator.manage_roles
# c.DummyAuthenticator.manage_roles = False

## 
#  See also: Authenticator.otp_prompt
# c.DummyAuthenticator.otp_prompt = 'OTP:'

## .. deprecated:: 5.3
#  
#      Setting a password in DummyAuthenticator is deprecated.
#      Use `SharedPasswordAuthenticator` instead.
#  Default: ''
# c.DummyAuthenticator.password = ''

## 
#  See also: Authenticator.post_auth_hook
# c.DummyAuthenticator.post_auth_hook = None

## Force refresh of auth prior to spawn.
#  See also: Authenticator.refresh_pre_spawn
# c.DummyAuthenticator.refresh_pre_spawn = False

## 
#  See also: Authenticator.request_otp
# c.DummyAuthenticator.request_otp = False

## Reset managed roles to result of `load_managed_roles()` on startup.
#  See also: Authenticator.reset_managed_roles_on_startup
# c.DummyAuthenticator.reset_managed_roles_on_startup = False

## Dictionary mapping authenticator usernames to JupyterHub users.
#  See also: Authenticator.username_map
# c.DummyAuthenticator.username_map = {}

## 
#  See also: Authenticator.username_pattern
# c.DummyAuthenticator.username_pattern = ''

## Deprecated, use `Authenticator.allowed_users`
#  See also: Authenticator.whitelist
# c.DummyAuthenticator.whitelist = set()

#------------------------------------------------------------------------------
# LocalAuthenticator(Authenticator) configuration
#------------------------------------------------------------------------------
## Base class for Authenticators that work with local Linux/UNIX users
#  
#      Checks for local users, and can attempt to create them if they exist.

## The command to use for creating users as a list of strings
#  
#  For each element in the list, the string USERNAME will be replaced with the
#  user's username. The username will also be appended as the final argument.
#  
#  For Linux, the default value is:
#  
#      ['adduser', '-q', '--gecos', '""', '--disabled-password']
#  
#  To specify a custom home directory, set this to:
#  
#      ['adduser', '-q', '--gecos', '""', '--home', '/customhome/USERNAME', '--
#  disabled-password']
#  
#  This will run the command:
#  
#      adduser -q --gecos "" --home /customhome/river --disabled-password river
#  
#  when the user 'river' is created.
#  Default: []
# c.LocalAuthenticator.add_user_cmd = []

## 
#  See also: Authenticator.admin_users
# c.LocalAuthenticator.admin_users = set()

## 
#  See also: Authenticator.allow_all
# c.LocalAuthenticator.allow_all = False

## 
#  See also: Authenticator.allow_existing_users
# c.LocalAuthenticator.allow_existing_users = False

## Allow login from all users in these UNIX groups.
#  
#  .. versionchanged:: 5.0
#      `allowed_groups` may be specified together with allowed_users,
#      to grant access by group OR name.
#  Default: set()
# c.LocalAuthenticator.allowed_groups = set()

## 
#  See also: Authenticator.allowed_users
# c.LocalAuthenticator.allowed_users = set()

## Is there any allow config?
#  See also: Authenticator.any_allow_config
# c.LocalAuthenticator.any_allow_config = False

## The max age (in seconds) of authentication info
#  See also: Authenticator.auth_refresh_age
# c.LocalAuthenticator.auth_refresh_age = 300

## Automatically begin the login process
#  See also: Authenticator.auto_login
# c.LocalAuthenticator.auto_login = False

## 
#  See also: Authenticator.auto_login_oauth2_authorize
# c.LocalAuthenticator.auto_login_oauth2_authorize = False

## 
#  See also: Authenticator.blocked_users
# c.LocalAuthenticator.blocked_users = set()

## If set to True, will attempt to create local system users if they do not exist
#  already.
#  
#  Supports Linux and BSD variants only.
#  Default: False
# c.LocalAuthenticator.create_system_users = False

## Delete any users from the database that do not pass validation
#  See also: Authenticator.delete_invalid_users
# c.LocalAuthenticator.delete_invalid_users = False

## Enable persisting auth_state (if available).
#  See also: Authenticator.enable_auth_state
# c.LocalAuthenticator.enable_auth_state = False

## DEPRECATED: use allowed_groups
#  Default: set()
# c.LocalAuthenticator.group_whitelist = set()

## Let authenticator manage user groups
#  See also: Authenticator.manage_groups
# c.LocalAuthenticator.manage_groups = False

## Let authenticator manage roles
#  See also: Authenticator.manage_roles
# c.LocalAuthenticator.manage_roles = False

## 
#  See also: Authenticator.otp_prompt
# c.LocalAuthenticator.otp_prompt = 'OTP:'

## 
#  See also: Authenticator.post_auth_hook
# c.LocalAuthenticator.post_auth_hook = None

## Force refresh of auth prior to spawn.
#  See also: Authenticator.refresh_pre_spawn
# c.LocalAuthenticator.refresh_pre_spawn = False

## 
#  See also: Authenticator.request_otp
# c.LocalAuthenticator.request_otp = False

## Reset managed roles to result of `load_managed_roles()` on startup.
#  See also: Authenticator.reset_managed_roles_on_startup
# c.LocalAuthenticator.reset_managed_roles_on_startup = False

## Dictionary of uids to use at user creation time. This helps ensure that users
#  created from the database get the same uid each time they are created in
#  temporary deployments or containers.
#  Default: {}
# c.LocalAuthenticator.uids = {}

## Dictionary mapping authenticator usernames to JupyterHub users.
#  See also: Authenticator.username_map
# c.LocalAuthenticator.username_map = {}

## 
#  See also: Authenticator.username_pattern
# c.LocalAuthenticator.username_pattern = ''

## Deprecated, use `Authenticator.allowed_users`
#  See also: Authenticator.whitelist
# c.LocalAuthenticator.whitelist = set()

#------------------------------------------------------------------------------
# PAMAuthenticator(LocalAuthenticator) configuration
#------------------------------------------------------------------------------
## Authenticate local UNIX users with PAM

## 
#  See also: LocalAuthenticator.add_user_cmd
# c.PAMAuthenticator.add_user_cmd = []

## Authoritative list of user groups that determine admin access. Users not in
#  these groups can still be granted admin status through admin_users.
#  
#  allowed/blocked rules still apply.
#  
#  Note: As of JupyterHub 2.0, full admin rights should not be required, and more
#  precise permissions can be managed via roles.
#  Default: set()
# c.PAMAuthenticator.admin_groups = set()

## 
#  See also: Authenticator.admin_users
# c.PAMAuthenticator.admin_users = set()

## 
#  See also: Authenticator.allow_all
# c.PAMAuthenticator.allow_all = False

## 
#  See also: Authenticator.allow_existing_users
# c.PAMAuthenticator.allow_existing_users = False

## 
#  See also: LocalAuthenticator.allowed_groups
# c.PAMAuthenticator.allowed_groups = set()

## 
#  See also: Authenticator.allowed_users
# c.PAMAuthenticator.allowed_users = set()

## Is there any allow config?
#  See also: Authenticator.any_allow_config
# c.PAMAuthenticator.any_allow_config = False

## The max age (in seconds) of authentication info
#  See also: Authenticator.auth_refresh_age
# c.PAMAuthenticator.auth_refresh_age = 300

## Automatically begin the login process
#  See also: Authenticator.auto_login
# c.PAMAuthenticator.auto_login = False

## 
#  See also: Authenticator.auto_login_oauth2_authorize
# c.PAMAuthenticator.auto_login_oauth2_authorize = False

## 
#  See also: Authenticator.blocked_users
# c.PAMAuthenticator.blocked_users = set()

## Whether to check the user's account status via PAM during authentication.
#  
#  The PAM account stack performs non-authentication based account management. It
#  is typically used to restrict/permit access to a service and this step is
#  needed to access the host's user access control.
#  
#  Disabling this can be dangerous as authenticated but unauthorized users may be
#  granted access and, therefore, arbitrary execution on the system.
#  Default: True
# c.PAMAuthenticator.check_account = True

## 
#  See also: LocalAuthenticator.create_system_users
# c.PAMAuthenticator.create_system_users = False

## Delete any users from the database that do not pass validation
#  See also: Authenticator.delete_invalid_users
# c.PAMAuthenticator.delete_invalid_users = False

## Enable persisting auth_state (if available).
#  See also: Authenticator.enable_auth_state
# c.PAMAuthenticator.enable_auth_state = False

## The text encoding to use when communicating with PAM
#  Default: 'utf8'
# c.PAMAuthenticator.encoding = 'utf8'

## Number of executor threads.
#  
#  PAM auth requests happen in this thread, so it is mostly waiting for the pam
#  stack. One thread is usually enough, unless your pam stack is doing something
#  slow like network requests
#  Default: 4
# c.PAMAuthenticator.executor_threads = 4

## DEPRECATED: use allowed_groups
#  See also: LocalAuthenticator.group_whitelist
# c.PAMAuthenticator.group_whitelist = set()

## Let authenticator manage user groups
#  See also: Authenticator.manage_groups
# c.PAMAuthenticator.manage_groups = False

## Let authenticator manage roles
#  See also: Authenticator.manage_roles
# c.PAMAuthenticator.manage_roles = False

## Whether to open a new PAM session when spawners are started.
#  
#  This may trigger things like mounting shared filesystems, loading credentials,
#  etc. depending on system configuration.
#  
#  The lifecycle of PAM sessions is not correct, so many PAM session
#  configurations will not work.
#  
#  If any errors are encountered when opening/closing PAM sessions, this is
#  automatically set to False.
#  
#  .. versionchanged:: 2.2
#  
#      Due to longstanding problems in the session lifecycle,
#      this is now disabled by default.
#      You may opt-in to opening sessions by setting this to True.
#  Default: False
# c.PAMAuthenticator.open_sessions = False

## 
#  See also: Authenticator.otp_prompt
# c.PAMAuthenticator.otp_prompt = 'OTP:'

## Round-trip the username via PAM lookups to make sure it is unique
#  
#  PAM can accept multiple usernames that map to the same user, for example
#  DOMAIN\username in some cases.  To prevent this, convert username into uid,
#  then back to uid to normalize.
#  Default: False
# c.PAMAuthenticator.pam_normalize_username = False

## 
#  See also: Authenticator.post_auth_hook
# c.PAMAuthenticator.post_auth_hook = None

## Force refresh of auth prior to spawn.
#  See also: Authenticator.refresh_pre_spawn
# c.PAMAuthenticator.refresh_pre_spawn = False

## 
#  See also: Authenticator.request_otp
# c.PAMAuthenticator.request_otp = False

## Reset managed roles to result of `load_managed_roles()` on startup.
#  See also: Authenticator.reset_managed_roles_on_startup
# c.PAMAuthenticator.reset_managed_roles_on_startup = False

## The name of the PAM service to use for authentication
#  Default: 'login'
# c.PAMAuthenticator.service = 'login'

## 
#  See also: LocalAuthenticator.uids
# c.PAMAuthenticator.uids = {}

## Dictionary mapping authenticator usernames to JupyterHub users.
#  See also: Authenticator.username_map
# c.PAMAuthenticator.username_map = {}

## 
#  See also: Authenticator.username_pattern
# c.PAMAuthenticator.username_pattern = ''

## Deprecated, use `Authenticator.allowed_users`
#  See also: Authenticator.whitelist
# c.PAMAuthenticator.whitelist = set()

#------------------------------------------------------------------------------
# SharedPasswordAuthenticator(Authenticator) configuration
#------------------------------------------------------------------------------
## Authenticator with static shared passwords.
#  
#  For use in short-term deployments with negligible security concerns.
#  
#  Enable with::
#  
#      c.JupyterHub.authenticator_class = "shared-password"
#  
#  .. warning::
#      This is an insecure Authenticator only appropriate for short-term
#      deployments with no requirement to protect users from each other.
#  
#      - The password is stored in plain text at rest in config
#      - Anyone with the password can login as **any user**
#      - All users are able to login as all other (non-admin) users with the same password

## Set a global password that grants *admin* privileges to users logging in with
#  this password. Only usernames declared in `admin_users` may login with this
#  password.
#  
#  Must meet the following requirements:
#  
#  - Be 32 characters or longer - Not be the same as `user_password`
#  
#  If not set, admin users cannot login.
#  Default: None
# c.SharedPasswordAuthenticator.admin_password = None

## 
#  See also: Authenticator.admin_users
# c.SharedPasswordAuthenticator.admin_users = set()

## 
#  See also: Authenticator.allow_all
# c.SharedPasswordAuthenticator.allow_all = False

## 
#  See also: Authenticator.allow_existing_users
# c.SharedPasswordAuthenticator.allow_existing_users = False

## 
#  See also: Authenticator.allowed_users
# c.SharedPasswordAuthenticator.allowed_users = set()

## Is there any allow config?
#  See also: Authenticator.any_allow_config
# c.SharedPasswordAuthenticator.any_allow_config = False

## The max age (in seconds) of authentication info
#  See also: Authenticator.auth_refresh_age
# c.SharedPasswordAuthenticator.auth_refresh_age = 300

## Automatically begin the login process
#  See also: Authenticator.auto_login
# c.SharedPasswordAuthenticator.auto_login = False

## 
#  See also: Authenticator.auto_login_oauth2_authorize
# c.SharedPasswordAuthenticator.auto_login_oauth2_authorize = False

## 
#  See also: Authenticator.blocked_users
# c.SharedPasswordAuthenticator.blocked_users = set()

## Delete any users from the database that do not pass validation
#  See also: Authenticator.delete_invalid_users
# c.SharedPasswordAuthenticator.delete_invalid_users = False

## Enable persisting auth_state (if available).
#  See also: Authenticator.enable_auth_state
# c.SharedPasswordAuthenticator.enable_auth_state = False

## Let authenticator manage user groups
#  See also: Authenticator.manage_groups
# c.SharedPasswordAuthenticator.manage_groups = False

## Let authenticator manage roles
#  See also: Authenticator.manage_roles
# c.SharedPasswordAuthenticator.manage_roles = False

## 
#  See also: Authenticator.otp_prompt
# c.SharedPasswordAuthenticator.otp_prompt = 'OTP:'

## 
#  See also: Authenticator.post_auth_hook
# c.SharedPasswordAuthenticator.post_auth_hook = None

## Force refresh of auth prior to spawn.
#  See also: Authenticator.refresh_pre_spawn
# c.SharedPasswordAuthenticator.refresh_pre_spawn = False

## 
#  See also: Authenticator.request_otp
# c.SharedPasswordAuthenticator.request_otp = False

## Reset managed roles to result of `load_managed_roles()` on startup.
#  See also: Authenticator.reset_managed_roles_on_startup
# c.SharedPasswordAuthenticator.reset_managed_roles_on_startup = False

## Set a global password for all *non admin* users wanting to log in.
#  
#  Must be 8 characters or longer.
#  
#  If not set, regular users cannot login.
#  
#  If `allow_all` is True, anybody can register unlimited new users with any
#  username by logging in with this password. Users may be allowed by name by
#  specifying `allowed_users`.
#  
#  Any user will also be able to login as **any other non-admin user** with this
#  password.
#  
#  If `admin_users` is set, those users *must* use `admin_password` to log in.
#  Default: None
# c.SharedPasswordAuthenticator.user_password = None

## Dictionary mapping authenticator usernames to JupyterHub users.
#  See also: Authenticator.username_map
# c.SharedPasswordAuthenticator.username_map = {}

## 
#  See also: Authenticator.username_pattern
# c.SharedPasswordAuthenticator.username_pattern = ''

## Deprecated, use `Authenticator.allowed_users`
#  See also: Authenticator.whitelist
# c.SharedPasswordAuthenticator.whitelist = set()

#------------------------------------------------------------------------------
# CryptKeeper(SingletonConfigurable) configuration
#------------------------------------------------------------------------------
## Encapsulate encryption configuration
#  
#      Use via the encryption_config singleton below.

#  Default: []
# c.CryptKeeper.keys = []

## The number of threads to allocate for encryption
#  Default: 16
# c.CryptKeeper.n_threads = 16
