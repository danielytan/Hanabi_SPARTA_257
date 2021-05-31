#!/usr/bin/env python3

# Custom code to produce graphs to compare average scores and perfect game rates 
# of various blueprint policies with and without search techniques from SPARTA.

import math
import numpy as np
import matplotlib.pyplot as plt

"""
A little utility script to create graphs for results from accum_scores
"""

def experiment_avg_score():
    plt.figure()
    labels = ['SmartBot', 'SAD']
    nosearch_means = [23.048, 24.076]
    singleagent_means = [23.9393, 24.72]

    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, nosearch_means, width, label='No Search')
    rects2 = ax.bar(x + width/2, singleagent_means, width, label='Single-Agent Search')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Average Scores')
    ax.set_xlabel('Blueprint Policies')
    ax.set_title('Average scores by blueprint policy')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend(loc="lower left")

    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)

    fig.tight_layout()
    plt.savefig('figures/experiment_average_scores.png')

def experiment_perfect_game_percent():
    plt.figure()
    labels = ['SmartBot', 'SAD']
    nosearch_perfect_rates = [29.32, 56.54]
    singleagent_perfect_rates = [57.91, 69.12]

    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, nosearch_perfect_rates, width, label='No Search')
    rects2 = ax.bar(x + width/2, singleagent_perfect_rates, width, label='Single-Agent Search')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Perfect Game %')
    ax.set_xlabel('Blueprint Policies')
    ax.set_title('Perfect game % by blueprint policy')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)

    fig.tight_layout()
    plt.savefig('figures/experiment_perfect_game_rates.png')

def extension_avg_score():
    plt.figure()
    labels = ['HolmesBot', 'SimpleBot', 'SmartBot']
    nosearch_means = [20.637, 16.905, 23.048]
    singleagent_means = [22.9286, 0, 23.9393]

    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, nosearch_means, width, label='No Search')
    rects2 = ax.bar(x + width/2, singleagent_means, width, label='Single-Agent Search')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Average Scores')
    ax.set_xlabel('Blueprint Policies')
    ax.set_title('Average scores by blueprint policy')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)

    fig.tight_layout()
    plt.savefig('figures/extension_average_scores.png')

def extension_perfect_game_percent():
    plt.figure()
    labels = ['HolmesBot', 'SimpleBot', 'SmartBot']
    nosearch_perfect_rates = [4.80, 0, 29.32]
    singleagent_perfect_rates = [23.81, 0, 57.91]

    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, nosearch_perfect_rates, width, label='No Search')
    rects2 = ax.bar(x + width/2, singleagent_perfect_rates, width, label='Single-Agent Search')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Perfect Game %')
    ax.set_xlabel('Blueprint Policies')
    ax.set_title('Perfect game % by blueprint policy')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)

    fig.tight_layout()
    plt.savefig('figures/extension_perfect_game_rates.png')

def make_graphs():
    experiment_avg_score()
    experiment_perfect_game_percent()
    extension_avg_score()
    extension_perfect_game_percent()

if __name__ == "__main__":
    make_graphs()
