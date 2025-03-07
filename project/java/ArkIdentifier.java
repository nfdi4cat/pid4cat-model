package None;

import java.util.List;
import lombok.*;



/* version: 0.0.0 */


/**
  An ARK (Archival Resource Key).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ArkIdentifier extends RelatedIdentifier {

  private String identifier;
  private String resolvingUrl;

}
