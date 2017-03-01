'use strict';


module.exports = function (grunt) {
    require('time-grunt')(grunt);

    require('jit-grunt')(grunt, {
        cdnify: 'grunt-google-cdn'
    });

    grunt.loadNpmTasks('grunt-connect-proxy');

    var modRewrite = require('connect-modrewrite');

    var appConfig = {
        app: require('./bower.json').appPath || 'app',
        dist: 'dist'
    };

    grunt.initConfig({
        app: appConfig,

        watch: {
            bower: {
                files: ['bower.json'],
                tasks: ['wiredep']
            },
            js: {
                files: ['<%= app.app %>/assets/js/{,*/}*.js', '!app/assets/js/libs/{,*/}*.js'],
                tasks: ['newer:jshint:all'],
            },
            gruntfile: {
                files: ['Gruntfile.js']
            },
            // compass: {
            //     files: ['<%= app.app %>/assets/styles/{,*/}*.{scss,sass}'],
            //     tasks: ['compass:server', 'postcss:server']
            // },
            livereload: {
                options: {
                    livereload: '<%= connect.options.livereload %>'
                },
                files: [
                    '<%= app.app %>/{,*/}*.html',
                    '<%= app.app %>/**/{,*/}*.html',
                    '<%= app.app %>/assets/css/{,*/}*.css',
                    '<%= app.app %>/assets/js/{,*/}*.html',
                    '<%= app.app %>/assets/img/{,*/}*.{png,jpg,jpeg,gif,webp,svg}'
                ]
            },
            jsTest: {
              files: ['test/spec/{,*/}*.js'],
              tasks: ['newer:jshint:test', 'karma']
            }
        },

        // The actual grunt server settings
        connect: {
          options: {
            port: 9000,
            // Change this to '0.0.0.0' to access the server from outside.
            hostname: 'localhost',
            livereload: 35729,
            middleware: function() {
              return [function(req, res) {
                require('fs').createReadStream('app/index.html').pipe(res);
              }];
            }
          },
          server: {
            proxies: [
              {
                context: '/api',
                host: '127.0.0.1',
                port: 8000,
                https: false,
                xforward: false,
                hideHeaders: ['x-removed-header']
              }
            ]
          },
          livereload: {
            options: {
              open: true,
              middleware: function(connect) {
                var middlewares = [];

                middlewares = [
                  require('grunt-connect-proxy/lib/utils').proxyRequest,
                  modRewrite(['!/api|\\.jpg|\\.gif|\\.png|\\.svg|\\.woff2|\\.eot|\\.html|\\.js|\\.css|\\.woff|\\.ttf|\\.swf$ /index.html [L]']),
                  connect.static('.tmp'),
                  connect().use(
                    '/app/assets/bower_components',
                    connect.static('./app/assets/bower_components')
                  ),
                  connect.static(appConfig.app)
                ];

                return middlewares;

              }
            }
          },
          test: {
            options: {
              port: 9001,
              middleware: function (connect) {
                return [
                  connect.static('.tmp'),
                  connect.static('test'),
                  connect().use(
                    './app/assets/bower_components',
                    connect.static('./app/assets/bower_components')
                  ),
                  connect.static(appConfig.app)
                ];
              }
            }
          }
          // dist: {
          //   options: {
          //     open: true,
          //     base: '<%= app.dist %>'
          //   }
          // }
        },

        jshint: {
            options: {
                jshintrc: '.jshintrc',
                reporter: require('jshint-stylish')
            },
            all: {
                src: [
                    'Gruntfile.js',
                    '<%= app.app %>/assets/js/{,*/}*.js'
                ]
            },
            test: {
                options: {
                    jshintrc: 'test/.jshintrc',
                    reporterOutput: ''
                },
                src: ['test/spec/{,*/}*.js']
            }
        },

        // Make sure code styles are up to par
      jscs: {
        options: {
          config: '.jscsrc',
          verbose: true
        },
        all: {
          src: [
            'Gruntfile.js',
            '<%= app.app %>/assets/js/{,*/}*.js'
          ]
        },
        test: {
          src: ['test/spec/{,*/}*.js']
        }
      },

      // Empties folders to start fresh
      clean: {
        dist: {
          files: [{
            dot: true,
            src: [
              '.tmp',
              '<%= app.dist %>/{,*/}*',
              '!<%= app.dist %>/.git{,*/}*'
            ]
          }]
        },
        server: '.tmp'
      },

        // Add vendor prefixed styles
        // autoprefixer: {
        //   options: {
        //     browsers: ['last 1 version']
        //   },
        //   dist: {
        //     files: [{
        //       expand: true,
        //       cwd: '<%= app.app %>/assets/styles/',
        //       src: '{,*/}*.css',
        //       dest: '<%= app.app %>/assets/styles/'
        //     }]
        //   }
        // },

        // Add vendor prefixed styles
        postcss: {
          options: {
            processors: [
              require('autoprefixer-core')({browsers: ['last 1 version']})
            ]
          },
          server: {
            options: {
              map: true
            },
            files: [{
              expand: true,
              cwd: '.tmp/styles/',
              src: '{,*/}*.css',
              dest: '.tmp/styles/'
            }]
          },
          dist: {
            files: [{
              expand: true,
              cwd: '.tmp/styles/',
              src: '{,*/}*.css',
              dest: '.tmp/styles/'
            }]
          }
        },

        wiredep: {
            target: {
                src: ['<%= app.app %>/index.html'],
                ignorePath:  /\.\./
            },
            test: {
                devDependencies: true,
                src: '<%= karma.unit.configFile %>',
                ignorePath:  /\.\.\//,
                fileTypes:{
                    js: {
                        block: /(([\s\t]*)\/{2}\s*?bower:\s*?(\S*))(\n|\r|.)*?(\/{2}\s*endbower)/gi,
                        detect: {
                            js: /'(.*\.js)'/gi
                        },
                        replace: {
                            js: '\'{{filePath}}\','
                        }
                    }
                }
            },
            sass: {
                src: ['<%= app.app %>/assets/styles/{,*/}*.{scss,sass}'],
                ignorePath: /(\.\.\/){1,2}bower_components\//
            }
        },

        // Compiles Sass to CSS and generates necessary files if requested
        compass: {
          options: {
            sassDir: '<%= app.app %>/assets/styles',
            cssDir: '<%= app.app %>/assets/css',
            // generatedImagesDir: '<%= app.app %>/assets/.tmp/img/generated',
            imagesDir: '<%= app.app %>/assets/img',
            javascriptsDir: '<%= app.app %>/assets/js',
            fontsDir: '<%= app.app %>/styles/fonts',
            importPath: '<%= app.app %>/assets/bower_components',
            httpImagesPath: '/img',
            httpGeneratedImagesPath: '/img/generated',
            httpFontsPath: '/styles/fonts',
            relativeAssets: false,
            assetCacheBuster: false,
            raw: 'Sass::Script::Number.precision = 10\n'
          },
          dist: {
            options: {
              generatedImagesDir: '<%= app.dist %>/images/generated'
            }
          },
          server: {
            options: {
              debugInfo: true,
              sourcemap: true
            }
          }
        },
        cdnify: {
            dist: {
                html: ['<%= app.app %>/index.html']
            }
        },
        copy: {
            styles: {
            expand: true,
            cwd: '<%= app.app %>/assets/styles',
            dest: '<%= app.app %>/assets/css/',
            src: '{,*/}*.css'
          }
        },
        // Run some tasks in parallel to speed up the build process
        concurrent: {
          server: [
            // 'compass:server'
          ]
          // test: [
          //   'compass'
          // ],
          // dist: [
          //   'compass:dist',
          //   'imagemin',
          //   'svgmin'
          // ]
        },
        karma: {
            unit: {
                configFile: 'test/karma.conf.js',
                singleRun: true
            }
        }
    });
    
    grunt.registerTask('serve', 'Compile then start a connect web server', function (target) {
        if (target === 'dist') {
            return grunt.task.run(['build', 'connect:dist:keepalive']);
        }

        grunt.task.run([
            'clean:server',
            'wiredep',
            'concurrent:server',
            'postcss',
            'configureProxies:server',
            'connect:livereload',
            'watch'
        ]);
    });
};