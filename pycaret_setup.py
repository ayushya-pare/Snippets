# PyCaret setup
exp_clf = setup(data=data, 
                target='',  # Target variable
                imputation_type='simple',  # 'simple', 'iterative'
                numeric_imputation='mean',  # 'mean', 'median', 'zero'
                categorical_imputation='mode',  # 'constant', 'mode'
                normalize=True,  # True, False
                normalize_method='zscore',  # 'zscore', 'minmax', 'maxabs', 'robust'
                transformation=True,  # True, False
                transformation_method='yeo-johnson',  # 'yeo-johnson', 'quantile'
                remove_outliers=True,  # True, False
                outliers_threshold=0.05,  # Threshold for outlier removal
                combine_rare_levels=True,  # True, False
                rare_level_threshold=0.1,  # Threshold for combining rare levels
                polynomial_features=True,  # True, False
                polynomial_degree=2,  # Degree for polynomial features
                trigonometry_features=True,  # True, False
                feature_interaction=True,  # True, False
                feature_ratio=True,  # True, False
                feature_selection=True,  # True, False
                feature_selection_threshold=0.8,  # Threshold for feature selection
                pca=True,  # True, False
                pca_method='linear',  # 'linear', 'kernel', 'incremental'
                pca_components=0.99,  # Number of components or variance to keep
                ignore_low_variance=True,  # True, False
                remove_multicollinearity=True,  # True, False
                multicollinearity_threshold=0.9,  # Threshold for multicollinearity
                bin_numeric_features=None,  # List of numeric features to bin
                remove_perfect_collinearity=True,  # True, False
                create_clusters=False,  # True, False
                cluster_iter=20,  # Number of iterations for clustering
                polynomial_threshold=0.1,  # Threshold for polynomial features
                group_features=None,  # List of features to group
                group_names=None,  # List of group names
                custom_pipeline=None,  # Custom pipeline
                custom_data=None,  # Custom data
                silent=False,  # True, False
                verbose=True,  # True, False
                profile=False,  # True, False
                session_id=123)


best_models = compare_models(
    fold = 5,
    n_select=3,
)

# choose the best model- create the best model (train_data) - tune the model

# best model = Ridge
best_model = best_models[0]
best_model

# Create model

best_model_ = create_model('knn',fold = 5)

# tune model

tuned_model = tune_model(best_model_, fold = 5)

# Evaluate and visualize - class. report, AUC, feature,

plot_model(tuned_model, plot='confusion_matrix')

plot_model(tuned_model, plot='auc')



# Predict using test data with the best model (test_data)

predict_model(tuned_model)

# Finalize model - fit onto the complete dataset

final_model = finalize_model(tuned_model)

# Save the finalized model

save_model(final_model,'final model')

# load the model and fit onto the new dataset

final_model_ = load_model('final model')
