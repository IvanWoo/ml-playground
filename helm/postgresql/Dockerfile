# https://github.com/pgvector/pgvector/issues/126#issuecomment-1589203644
ARG BITNAMI_POSTGRES_BASE_VERSION=15
FROM bitnami/postgresql:$BITNAMI_POSTGRES_BASE_VERSION as build
ARG BITNAMI_POSTGRES_BASE_VERSION
ARG PGVECTOR_VERSION=v0.4.4

USER root

RUN set -e; \
    install_packages build-essential git ; \
    git clone --branch $PGVECTOR_VERSION https://github.com/pgvector/pgvector.git /tmp/pgvector ; \
    cd /tmp/pgvector ; \
    make OPTFLAGS="" ; \
    make install ; \
    :

FROM bitnami/postgresql:$BITNAMI_POSTGRES_BASE_VERSION

# Doc
COPY --from=build \
    /tmp/pgvector/README.md \
    /tmp/pgvector/LICENSE \
    /usr/share/doc/pgvector/
# Code
COPY --from=build \
    /tmp/pgvector/vector.so \
    /opt/bitnami/postgresql/lib/
COPY --from=build \
    /tmp/pgvector/vector.control \
    /opt/bitnami/postgresql/share/extension/
COPY --from=build \
    /tmp/pgvector/sql/*.sql \
    /opt/bitnami/postgresql/share/extension/
