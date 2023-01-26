import setuptools

setuptools.setup(
    name="anaconda.enterprise.server.common.sdk",
    version="0.4.3",
    package_dir={"": "src"},
    packages=setuptools.find_namespace_packages(where="src"),
    author="Joshua C. Burt",
    description="Anaconda Enterprise Server Common SDK",
    long_description="Anaconda Enterprise Server Common SDK",
    include_package_data=True,
    zip_safe=False,
)
