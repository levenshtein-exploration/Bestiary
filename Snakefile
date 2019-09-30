
W_SIZES = list(range(1, 10))
A_SIZES = list(range(2, 5))
Ks = list(range(1, 3))

rule all:
    input:
        "data/results/file_list.txt"
        # expand("data/results/a{a}_n{s}.tsv", a=A_SIZES, s=W_SIZES)


rule leviewer_file:
    input:
        expand("data/results/a{a}_n{s}.tsv", a=A_SIZES, s=W_SIZES)
    output:
        "data/results/file_list.txt"
    run:
        shell("echo '' > {output}")
        for elem in input:
            shell(f"echo {elem.split('/')[-1]} >> {{output}}")


rule aglomerate_results:
    input:
        "data/a={a}/n={s}/global_count.tsv"
    output:
        "data/results/a{a}_n{s}.tsv"
    shell:
        "cp {input} {output}"


rule global_count:
    input:
        words="{workdir}/wordlist.txt",
        counts=expand("{{workdir}}/counts_{k}.tsv", k=Ks)
    output:
        "{workdir}/global_count.tsv"
    shell:
        "python3 merge_counts.py {input.words} {input.counts} > {output}"


rule wordborhood:
    input:
        words="{workdir}/a={a}/n={n}/wordlist.txt",
    output:
        "{workdir}/a={a}/n={n}/counts_{k}.tsv"
    shell:
        f"wordborhood -w {{input.words}} -a {{wildcards.a}} -d {config.get('dula_path')}/dula{{wildcards.k}}.fsm -k {{wildcards.k}} > {{output}}"


rule generate_words:
    output:
        "{workdir}/a={a}/n={n}/wordlist.txt"
    shell:
        "python3 list_words.py -a {wildcards.a} -n {wildcards.n} > {output}"
