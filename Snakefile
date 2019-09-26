
W_SIZES = list(range(1, 5))
A_SIZES = list(range(2, 5))
Ks = list(range(1, 3))

rule all:
    input:
        expand("data/a={a}/n={s}/global_count.tsv", a=A_SIZES, s=W_SIZES)


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
