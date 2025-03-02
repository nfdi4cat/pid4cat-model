package None;

import java.util.List;
import lombok.*;






/**
  A PURL (permanent uniform resource locator).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PurlIdentifier extends RelatedIdentifier {

  private String resolvingUrl;

}
