import nest.graphstatistics.basic_statistics
import nest.graphstatistics.spectral
import nest.graphstatistics.motif_measures
import nest.graphstatistics.path_statistics
import nest.graphstatistics.centrality
import nest.graphstatistics.community
import nest.graphstatistics.edge_activity
import nest.graphstatistics.initial_visualisation

# comment these lines to disable analysis modules
# For speed you might want to comment the spectral methods
# as I didnt have time to optimise them
statModules = [initial_visualisation, basic_statistics,
               spectral,
               motif_measures,
               path_statistics,
               edge_activity,
               centrality, community]
