# Autogenerated by nbdev

d = { 'settings': { 'allowed_cell_metadata_keys': '',
                'allowed_metadata_keys': '',
                'audience': 'Developers',
                'author': 'Thinking Machines Data Sciences Inc.',
                'author_email': 'geowrangler@thinkingmachin.es',
                'black_compat': 'True',
                'black_formatting': 'False',
                'branch': 'master',
                'clean_ids': 'True',
                'copyright': 'Thinking Machines Data Sciences Inc.',
                'custom_sidebar': 'True',
                'description': 'Tools for dealing with geospatial data',
                'doc_baseurl': '/',
                'doc_host': 'https://geowrangler.web.app',
                'doc_path': 'docs',
                'git_url': 'https://github.com/thinkingmachines/geowrangler/tree/master/',
                'host': 'github',
                'jupyter_hooks': 'True',
                'keywords': 'geospatial tools',
                'language': 'English',
                'lib_name': 'geowrangler',
                'lib_path': 'geowrangler',
                'license': 'MIT',
                'min_python': '3.7',
                'nbs_path': 'notebooks',
                'readme_nb': 'index.ipynb',
                'recursive': 'False',
                'requirements': 'pandas geopandas fastcore h3',
                'status': '2',
                'title': 'geowrangler',
                'tst_flags': 'slow | no_test',
                'user': 'thinkingmachines',
                'version': '0.1.0-dev2'},
  'syms': { 'geowrangler.dhs': { 'geowrangler.dhs.generate_dhs_cluster_data': 'https://geowrangler.web.app/dhs.html#generate_dhs_cluster_data',
                                 'geowrangler.dhs.get_approximate_col_name': 'https://geowrangler.web.app/dhs.html#get_approximate_col_name'},
            'geowrangler.grids': { 'geowrangler.grids.BingTileGridGenerator': 'https://geowrangler.web.app/grids.html#bingtilegridgenerator',
                                   'geowrangler.grids.BingTileGridGenerator.generate_grid': 'https://geowrangler.web.app/grids.html#bingtilegridgenerator.generate_grid',
                                   'geowrangler.grids.BingTileGridGenerator.get_tiles_for_polygon': 'https://geowrangler.web.app/grids.html#bingtilegridgenerator.get_tiles_for_polygon',
                                   'geowrangler.grids.BingTileGridGenerator.tile_to_polygon': 'https://geowrangler.web.app/grids.html#bingtilegridgenerator.tile_to_polygon',
                                   'geowrangler.grids.H3GridGenerator': 'https://geowrangler.web.app/grids.html#h3gridgenerator',
                                   'geowrangler.grids.H3GridGenerator.generate_grid': 'https://geowrangler.web.app/grids.html#h3gridgenerator.generate_grid',
                                   'geowrangler.grids.H3GridGenerator.get_hexes_for_polygon': 'https://geowrangler.web.app/grids.html#h3gridgenerator.get_hexes_for_polygon',
                                   'geowrangler.grids.SquareGridBoundary': 'https://geowrangler.web.app/grids.html#squaregridboundary',
                                   'geowrangler.grids.SquareGridBoundary.get_range_subset': 'https://geowrangler.web.app/grids.html#squaregridboundary.get_range_subset',
                                   'geowrangler.grids.SquareGridGenerator': 'https://geowrangler.web.app/grids.html#squaregridgenerator',
                                   'geowrangler.grids.SquareGridGenerator.create_cell': 'https://geowrangler.web.app/grids.html#squaregridgenerator.create_cell',
                                   'geowrangler.grids.SquareGridGenerator.create_grid_for_polygon': 'https://geowrangler.web.app/grids.html#squaregridgenerator.create_grid_for_polygon',
                                   'geowrangler.grids.SquareGridGenerator.generate_grid': 'https://geowrangler.web.app/grids.html#squaregridgenerator.generate_grid'},
            'geowrangler.raster_zonal_stats': { 'geowrangler.raster_zonal_stats.create_raster_zonal_stats': 'https://geowrangler.web.app/raster_zonal_stats.html#create_raster_zonal_stats'},
            'geowrangler.validation': { 'geowrangler.validation.AreaValidator': 'https://geowrangler.web.app/validation.html#areavalidator',
                                        'geowrangler.validation.AreaValidator.check': 'https://geowrangler.web.app/validation.html#areavalidator.check',
                                        'geowrangler.validation.AreaValidator.fix': 'https://geowrangler.web.app/validation.html#areavalidator.fix',
                                        'geowrangler.validation.BaseValidator': 'https://geowrangler.web.app/validation.html#basevalidator',
                                        'geowrangler.validation.BaseValidator.check': 'https://geowrangler.web.app/validation.html#basevalidator.check',
                                        'geowrangler.validation.BaseValidator.fix': 'https://geowrangler.web.app/validation.html#basevalidator.fix',
                                        'geowrangler.validation.BaseValidator.get_check_arguments': 'https://geowrangler.web.app/validation.html#basevalidator.get_check_arguments',
                                        'geowrangler.validation.BaseValidator.skip': 'https://geowrangler.web.app/validation.html#basevalidator.skip',
                                        'geowrangler.validation.BaseValidator.validate': 'https://geowrangler.web.app/validation.html#basevalidator.validate',
                                        'geowrangler.validation.BaseValidator.validator_column_name': 'https://geowrangler.web.app/validation.html#basevalidator.validator_column_name',
                                        'geowrangler.validation.CrsBoundsValidator': 'https://geowrangler.web.app/validation.html#crsboundsvalidator',
                                        'geowrangler.validation.CrsBoundsValidator.check': 'https://geowrangler.web.app/validation.html#crsboundsvalidator.check',
                                        'geowrangler.validation.CrsBoundsValidator.fix': 'https://geowrangler.web.app/validation.html#crsboundsvalidator.fix',
                                        'geowrangler.validation.CrsBoundsValidator.get_check_arguments': 'https://geowrangler.web.app/validation.html#crsboundsvalidator.get_check_arguments',
                                        'geowrangler.validation.GeometryValidation': 'https://geowrangler.web.app/validation.html#geometryvalidation',
                                        'geowrangler.validation.GeometryValidation.validate_all': 'https://geowrangler.web.app/validation.html#geometryvalidation.validate_all',
                                        'geowrangler.validation.NullValidator': 'https://geowrangler.web.app/validation.html#nullvalidator',
                                        'geowrangler.validation.NullValidator.check': 'https://geowrangler.web.app/validation.html#nullvalidator.check',
                                        'geowrangler.validation.NullValidator.fix': 'https://geowrangler.web.app/validation.html#nullvalidator.fix',
                                        'geowrangler.validation.NullValidator.skip': 'https://geowrangler.web.app/validation.html#nullvalidator.skip',
                                        'geowrangler.validation.OrientationValidator': 'https://geowrangler.web.app/validation.html#orientationvalidator',
                                        'geowrangler.validation.OrientationValidator.check': 'https://geowrangler.web.app/validation.html#orientationvalidator.check',
                                        'geowrangler.validation.OrientationValidator.fix': 'https://geowrangler.web.app/validation.html#orientationvalidator.fix',
                                        'geowrangler.validation.SelfIntersectingValidator': 'https://geowrangler.web.app/validation.html#selfintersectingvalidator',
                                        'geowrangler.validation.SelfIntersectingValidator.check': 'https://geowrangler.web.app/validation.html#selfintersectingvalidator.check',
                                        'geowrangler.validation.SelfIntersectingValidator.fix': 'https://geowrangler.web.app/validation.html#selfintersectingvalidator.fix',
                                        'geowrangler.validation.ValidationError': 'https://geowrangler.web.app/validation.html#validationerror'},
            'geowrangler.vector_zonal_stats': { 'geowrangler.vector_zonal_stats.compute_quadkey': 'https://geowrangler.web.app/vector_zonal_stats.html#compute_quadkey',
                                                'geowrangler.vector_zonal_stats.create_bingtile_zonal_stats': 'https://geowrangler.web.app/vector_zonal_stats.html#create_bingtile_zonal_stats',
                                                'geowrangler.vector_zonal_stats.create_zonal_stats': 'https://geowrangler.web.app/vector_zonal_stats.html#create_zonal_stats'}}}