import os
import pandas as pd
import matplotlib.pyplot as plt

# PATHS

TFM_PATH = "/opt/shared/TFM"
DIRECTORY_PATH = os.path.join(TFM_PATH, "code")
AUXILIAR_DATA_PATH = os.path.join(TFM_PATH, "data", "auxiliar")
FIGURES_PATH = os.path.join(TFM_PATH, "data", "figures")
BBDD_PATH_1 = os.path.join(TFM_PATH, "data", "processed", "1_TWEETS_RAW_BY_CLUSTER")
BBDD_PATH_2 = os.path.join(TFM_PATH, "data", "processed", "2_TWEETS_PROCESSED")
BBDD_PATH_3 = os.path.join(TFM_PATH, "data", "processed", "3_TWEETS_EMBEDDED")
BBDD_PATH_4 = os.path.join(TFM_PATH, "data", "processed", "4_RESULTS")


FILENAME_3_2_SILHOUETTE = "3_2_silhouette.csv"
FILENAME_3_2_METRICS = "3_2_metrics.csv"
FILENAME_3_2_CLASSIFICATION = "3_2_classification.csv"
FILENAME_3_3_METRICS = "3_3_metrics.csv"
FILENAME_3_3_CLASSIFICATION = "3_3_classification.csv"


delimiter = "|"
n_clusters = 10
seed = 1712
vmax = 1000
vmin = 0

# AUXILIAR VARIABLES

NLP_parameters = {
    "stopchars": '!"#$%&\'()*+,-./0123456789:;<=>?@[\\]^_`{|}~¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ¶·¸¹º»¼½¾¿Æ×ØÞßæø‘’“”„•…€™',
    "stopwords": list(pd.read_csv(os.path.join(AUXILIAR_DATA_PATH, 'stopwords.txt'), header = None)[0]),
    "langauge": "es",
    "seed": seed,
    "min_similarity": 0.85,
    "min_frequency": 3,
    "bigrams_min_count": 100,
    "bigrams_threshold": 0.85,
    "bigrams_scoring": "npmi"
}

DR_models_to_perform = ["PCA_TSNE"]
# DR_models_to_perform = ["PCA", "TSNE", "PCA_TSNE"]

DR_models = {
    "PCA": {
        "tag": "PCA",
        "short_name": "PCA",
        "long_name": "Principal Component Analysis",
        "parameters": {
            "n_components": 2,
            "svd_solver": "auto",
            "seed": seed       
        }
    },
    "TSNE": {
        "tag": "TSNE",
        "short_name": "TSNE",
        "long_name": "t-distributed Stochastic Neighbor Embedding",
        "parameters": {
            "0": {
                "n_components": 2,
                "init": "pca",
                "perplexity": 40,
                "early_exageration": 25.0,
                "learning_rate": 400,
                "n_iter": 100000,
                "n_iter_without_progress": 1000,
                "n_jobs": -1,
                "random_state": seed,
                "verbose": 0
            },
            # "1": {
            #     "n_components": 2,
            #     "init": "pca",
            #     "perplexity": 60,
            #     "early_exageration": 10.0,
            #     "learning_rate": 300,
            #     "n_iter": 100000,
            #     "n_iter_without_progress": 2000,
            #     "n_jobs": -1,
            #     "random_state": seed,
            #     "verbose": 0
            # }
        }
    },
    "PCA_TSNE": {
        "tag": "PCA_TSNE",
        "short_name": "PCA + TSNE",
        "long_name": "Principal Component Analysis + t-distributed Stochastic Neighbor Embedding",
        "parameters": {
            "PCA": {
                "n_components": 400,
                "svd_solver": "auto",
                "seed": seed
            },
            "cumulative_variance_ratio": {
                "min": 0.04,
                "max": 0.1
            },
            "TSNE": {
                "0": {
                    "n_components": 2,
                    "init": "pca",
                    "perplexity": 40,
                    "early_exageration": 25.0,
                    "learning_rate": 400,
                    "n_iter": 100000,
                    "n_iter_without_progress": 1000,
                    "n_jobs": -1,
                    "random_state": seed,
                    "verbose": 0
                },
                # "1": {
                #     "n_components": 2,
                #     "init": "pca",
                #     "perplexity": 60,
                #     "early_exageration": 5.0,
                #     "learning_rate": 300,
                #     "n_iter": 100000,
                #     "n_iter_without_progress": 2000,
                #     "n_jobs": -1,
                #     "random_state": seed,
                #     "verbose": 0
                # }
            }
        }
    }
}

C_models_to_perform = ['KMEANS', 'AGLO', 'GMIXT']

C_models = {
    "KMEANS": {
        "tag": "KMEANS",
        "short_name": "K-Means",
        "long_name": "K-Means",
        "parameters": {
            "n_clusters": n_clusters,
            "init": "k-means++",
            "n_init": 10,
            "random_state": seed       
        }
    },
    "AGLO": {
        "tag": "AGLO",
        "short_name": "Agglomerative Clustering",
        "long_name": "Agglomerative Clustering",
        "parameters": {
            "n_clusters": n_clusters,
            "linkage": "ward",
            "random_state": seed       
        }
    },
    "GMIXT": {
        "tag": "GMIXT",
        "short_name": "Gaussian Mixtures",
        "long_name": "Gaussian Mixtures",
        "parameters": {
            "n_clusters": n_clusters,
            "covariance_type": "full",
            "init_params": "kmeans",
            "max_iter": 100000,
            "random_state": seed       
        }
    }
}    



# DATAFRAME VARIABLE'S NAMES

# VAR_embedded = []

# for abrs in dim_red_abrs:
#     VAR_embedded.append(abrs + '_1')
#     VAR_embedded.append(abrs + '_2')
    
# VAR_classification = []
    
# for abrs1 in clustering_abrs:
#     for abrs2 in dim_red_abrs:
#         VAR_classification.append(abrs1 + '_' + abrs2)

# FIGURE TITLES

# SUPTITLE_WF = "Top 50 words by frequence"
# SUPTITLE_WF_CLUSTER = "Top 20 words by frequence in each class"
# SUPTITLE_DR_SP = "Tweets in embedded spaces by CLUSTER_REAL"
# SUPTITLE_KFIXED_SC = "Silhouette coefficients for K-fixed classifications"
# SUPTITLE_KFIXED_SP = "Real classifications vs. K-fixed classifications"
# SUPTITLE_KFIXED_CM = "K-fixed classifications' Confusion Matrices"
# SUPTITLE_KFREE_SC = "Silhouette coefficients for K-optimized classifications"
# SUPTITLE_KFREE_SP = "Real classifications vs. K-optimized classifications"
# SUPTITLE_KFREE_CM = "K-optimized classifications' Confusion Matrices"
# SUPTITLE_KFREE_DBSCAN_SP = "Real classifications vs. DBSCAN classifications"
# SUPTITLE_KFREE_DBSCAN_CM = "DBSCAN classifications' Confusion Matrices"

# FIGURE FILENAMES

# FILENAME_WORD_FREQUENCY = "1_word_frequency.png"
# FILENAME_WORD_FREQUENCY_CLUSTER = "1_word_frequency_cluster.png"
# FILENAME_DR_SP = "2_scatterplot.png"
# FILENAME_KFIXED_SC = "3_1_silhouette.png"
# FILENAME_KFIXED_SP = "3_1_scatterplot.png"
# FILENAME_KFIXED_CM = "3_1_confusionmatrix.png"
# FILENAME_KFREE_SC = "3_2_silhouette.png"
# FILENAME_KFREE_SP = "3_2_scatterplot.png"
# FILENAME_KFREE_CM = "3_2_confusionmatrix.png"
# FILENAME_KFREE_DBSCAN_SP = "3_3_scatterplot.png"
# FILENAME_KFREE_DBSCAN_CM = "3_3_confusionmatrix.png"
# FILENAME_WORDCLOUDS = "4_wordclouds.png"

# COLOR PALETTES

my_palette = {
    "00": '#000000', "01": '#023eff', "02": '#ff7c00', "03": '#1ac938', "04": '#e8000b',
    "05": '#8b2be2', "06": '#9f4800', "07": '#f14cc1', "08": '#a3a3a3', "09": '#ffc400',
    "10": '#00d7ff', "11": '#db5f57', "12": '#db8557', "13": '#dbaa57', "14": '#dbd057',
    "15": '#c0db57', "16": '#9bdb57', "17": '#75db57', "18": '#57db5f', "19": '#57db85',
    "20": '#57dbaa', "21": '#57dbd0', "22": '#57c0db', "23": '#579bdb', "24": '#5775db',
    "25": '#5f57db', "26": '#8557db', "27": '#aa57db', "28": '#d057db', "29": '#db57c0',
    "30": '#db579b', "31": '#db5775'
}

clustering_colors = ['#00BFFF',     # COLOR FOR KMEANS
                     '#7FFF00',     # COLOR FOR AGLO
                     '#9400D3']     # COLOR FOR GMIXT

plt.rcParams.update({'font.size': 7})