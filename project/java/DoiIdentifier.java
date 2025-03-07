package None;

import java.util.List;
import lombok.*;



/* version: 0.0.0 */


/**
  A digital object identifier (DOI).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class DoiIdentifier extends RelatedIdentifier {

  private String resolvingUrl;
  private String identifier;

}
