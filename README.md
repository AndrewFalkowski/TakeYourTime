# AC/BO Hackathon - Project 3: Take Your Time
### Assessing the Impact of Investment More Compute Time in ACQF Optimization
Team Members: Andrew R. Falkowski, Carter Salbego, Ramsey Issa, Dr. Taylor D. Sparks
> 🚧 🚧 🚧  
> WARNING! This repository is under active development and is expected to undergo several changes in the coming weeks.  
> 🚧 🚧 🚧

## Motivation
Physical experiments are time and resource intensive, necessitiating care when selecting experimental parameters as you optimize towards a goal. Bayesian optimization is a great tool for improving the efficiency of experimental campaigns; however, it isn't without its shortcomings. In our experimentation we observed that random seed choice can have a profound impact on the performance and variability of a Bayesian optimization (BO) campaign. Below we simulate 10 BO campaigns on a synthetic categorial hartmann6 problem where initial points are fixed and each campaign is initialized with a different random seed and optimized with upper confidence bound. Despite identical starting values, we observe dramatic differences in campaign performance and the final solution found after 50 optimization iterations.

![seeded_campaigns](https://github.com/AndrewFalkowski/TakeYourTime/assets/3618750/74d95ff6-e20c-44b4-8e25-87e6c819568a)

Digging into the problem we found that this variation in performance stems from the acqusition function optimizer with different seeds resulting in different acquisition function values despite fixed starting values. We then sought to devise a means of improving the consistency of optimization campaigns and reducing stochasticity in optimizer outcomes.

## Solution Proposal

We propose a simple brute force approach to acquisition function optimization that we call Random Retries Optimization. In this scheme we select a pool of random seeds and iteratively intialize and optimize our acquisition function with each of the random seends, storing the seed-specifi optimization results. After the pool of random seeds has been exhausted, we select the parameters that gave the highest acuqisition function value and collect an observation at that point. This process is repeated at each step of the optimization campaign.

![random_retries](https://github.com/AndrewFalkowski/TakeYourTime/assets/3618750/ed879441-784c-4c57-9db4-c709aa2562e1)

## Results

To assess the performance of this approach we apply the method to the categorical hartmann6 problem shown above with the 10 seeds from each individual campaign used for the seed pool of the Random Retries Optimizer. We observe consistent performance that outperforms many fixed seed optimization campaigns, especially in few-shot optimization scenarios where evaluations are limited. It is noted, however, that the Random Retries campaign does not find the true optimum value in the observed trials. Given that Random Retries improves the likelihood of finding the theoretically optimal next experiment, we suspect that model representation of the inherently difficult problem might is deficient and that high performing cases in some sense get "lucky" in their ACQF optimizations. Thus, Random Retries does not guarantee you will perform the best, but can guard against performing the worst.

![random_retry_perf](https://github.com/AndrewFalkowski/TakeYourTime/assets/3618750/2553f592-de6f-49cd-b781-e4a8e39e4da9)

## Future Work

The work presented in this repository was completed over the course of two days, and is not indicative of a thorough investigation of the involved phenomena. We plan to extend this work and demonstrate Random Retries performance across a range of acquisition functions and synthetic problems. Additionally, we aim to quantify the value of sampling additional random seeds vs. compute time to provide practitioners with guidelines of how many random seeds to check. 

