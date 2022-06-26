from SigProfilerExtractor import sigpro as sig
import click


@click.command("extractor", help="Pass path to mutspec table in SigProfiler format and path to output directory. Script release signatures from mutspec and decompose it with COSMIC database")
@click.option("--mutspec", required=True, type=click.Path(True), help="Path to mutspec samples table (tsv)")
@click.option("--outdir", required=True, type=click.Path(False), help="Path to output directory")
@click.option("-m", "--max_signatures", default=5, show_default=True, type=int, help="Maximum number of signatures to release")
@click.option("-t", "--threads", default=-1, show_default=True, type=int, help="Number of threads to use")
def main(mutspec, outdir, max_signatures, threads):
    sig.sigProfilerExtractor(
        "matrix", outdir,
        mutspec,
        minimum_signatures=1,
        maximum_signatures=max_signatures,
        cpu=threads,
        gpu=False,
    )


if __name__ == "__main__":
    main()


# TODO add custom database selection
