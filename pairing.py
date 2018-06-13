DATA_DIR = "detected"
IMAGE_DIR = os.path.join(DATA_DIR, "train_resized")

image_groups = {}
for image_name in os.listdir(IMAGE_DIR):
    base_name = image_name[0:-2]
    group_name = base_name[0:4]
    if group_name in image_groups:
        image_groups[group_name].append(image_name)
    else:
        image_groups[group_name] = [image_name]

num_sim = 0
image_triples = []
group_list = sorted(list(image_groups.keys()))
for i, g in enumerate(group_list):
    if num_sim % 100 == 0:
        print("Generated {:d} pos + {:d} neg = {:d} total image triples"
              .format(num_sim, num_sim, 2*num_sim), end="\r")
    images_in_group = image_groups[g]
    for p in range(len(images_in_group)):
      images_all.append(images_in_group[p])
    # generate similar pairs
    sim_pairs_it = itertools.combinations(images_in_group, 2)
    # for each similar pair, generate a different pair
    for ref_image, sim_image in sim_pairs_it:
        image_triples.append((ref_image, sim_image, 1))
        num_sim += 1
        
	while True:
            j = np.random.randint(low=0, high=len(group_list), size=1)[0]
            if j != i: break
        dif_image_candidates = image_groups[group_list[j]]
        k = np.random.randint(low=0, high=len(dif_image_candidates), size=1)[0]
        dif_image = dif_image_candidates[k]
        image_triples.append((ref_image, dif_image, 0))
        
print("Generated {:d} pos + {:d} neg = {:d} total image triples, COMPLETE"
      .format(num_sim, num_sim, 2*num_sim))
